import asyncio
import time
from concurrent.futures import ThreadPoolExecutor

import aiohttp
import uvloop
import keyring
import requests


# --- GitHub Token Manager ---
class GitHubAuthManager:
    KEY_NAME: str = "github_appimage_installer"

    @staticmethod
    def get_token() -> str | None:
        token = keyring.get_password(GitHubAuthManager.KEY_NAME, "token")
        if not token:
            raise ValueError("GitHub token is missing. Please set it in the keyring.")
        return token

    @staticmethod
    def apply_auth(headers: dict[str, str]) -> dict[str, str]:
        try:
            token = GitHubAuthManager.get_token()
        except ValueError as e:
            print(f"Authentication Error: {e}")
            raise
        if token:
            headers["Authorization"] = f"Bearer {token}"
        return headers


# --- Configuration ---
REPOS = [
    "cli/cli",
    "pbek/QOwnNotes",
    "AppFlowy-IO/AppFlowy",
    "laurent22/joplin",
    "electron/electron",
    "microsoft/vscode",
    "flutter/flutter",
    "facebook/react",
    "tensorflow/tensorflow",
    "siyuan-note/siyuan",
    "kubernetes/kubernetes",
    "ansible/ansible",
    "grafana/grafana",
]
NUM_REQUESTS = 10


# --- Get Smallest Asset from Latest Release ---
def get_small_asset_url(repos: list[str]) -> list[str]:
    urls = []
    for repo in repos:
        api_url = f"https://api.github.com/repos/{repo}/releases/latest"
        headers = GitHubAuthManager.apply_auth({"Accept": "application/vnd.github+json"})
        resp = requests.get(api_url, headers=headers)
        if resp.status_code == 429:
            reset_time = resp.headers.get("X-RateLimit-Reset")
            if reset_time:
                wait_time = int(reset_time) - int(time.time())
                print(f"Rate limit exceeded for {repo}. Waiting for {wait_time} seconds...")
                time.sleep(max(wait_time, 1))
                continue
        resp.raise_for_status()

        rate_limit = resp.headers.get("X-RateLimit-Limit", "unknown")
        remaining = resp.headers.get("X-RateLimit-Remaining", "unknown")
        reset_time = resp.headers.get("X-RateLimit-Reset", "unknown")
        print(
            f"Repo: {repo}, Rate limit: {rate_limit}, Remaining: {remaining}, Reset: {reset_time}"
        )
        assets = resp.json().get("assets", [])
        # Pick smallest non-zero size asset
        if assets:
            smallest = sorted([a for a in assets if a["size"] > 0], key=lambda x: x["size"])[0]
            print(
                f"Using asset from {repo}: {smallest['name']} ({smallest['size'] / 1024:.1f} KB)"
            )
            urls.append(smallest["browser_download_url"])
    return urls


# --- Threaded Download ---
def sync_download(url, headers):
    for attempt in range(5):  # Retry up to 5 times
        try:
            r = requests.get(url, headers=headers)
            if r.status_code == 429:
                reset_time = int(r.headers.get("X-RateLimit-Reset", time.time() + 1))
                wait_time = reset_time - int(time.time())
                print(f"Rate limit exceeded. Retrying in {wait_time} seconds...")
                time.sleep(max(wait_time, 1))
                continue
            r.raise_for_status()
            return len(r.content)
        except requests.exceptions.RequestException as e:
            print(f"Attempt {attempt + 1} failed: {e}")
            if attempt == 4:
                raise


def threaded_benchmark(url, headers, num_requests):
    with ThreadPoolExecutor(max_workers=num_requests) as executor:
        futures = [executor.submit(sync_download, url, headers) for _ in range(num_requests)]
        sizes = [f.result() for f in futures]
    return sizes


# --- Async Download ---
async def async_download(session, url):
    for attempt in range(5):  # Retry up to 5 times
        try:
            async with session.get(url) as response:
                if response.status == 429:
                    reset_time = int(
                        response.headers.get("X-RateLimit-Reset", time.time() + 1)
                    )
                    wait_time = reset_time - int(time.time())
                    print(f"Rate limit exceeded. Retrying in {wait_time} seconds...")
                    await asyncio.sleep(max(wait_time, 1))
                    continue
                response.raise_for_status()
                data = await response.read()
                return len(data)
        except aiohttp.ClientError as e:
            print(f"Attempt {attempt + 1} failed: {e}")
            if attempt == 4:
                raise


async def async_benchmark(url, headers, num_requests):
    connector = aiohttp.TCPConnector(limit=num_requests, use_dns_cache=True)
    async with aiohttp.ClientSession(connector=connector, headers=headers) as session:
        tasks = [async_download(session, url) for _ in range(num_requests)]
        return await asyncio.gather(*tasks)


# --- Benchmark Orchestrator ---
def run_benchmark():
    print("🔐 Authenticating with GitHub...")
    headers = GitHubAuthManager.apply_auth({})

    print("📦 Fetching asset from repositories...")
    url = get_small_asset_url(REPOS)[0]  # Use the first available asset URL for consistency

    print(f"\n🚀 Running benchmark with {NUM_REQUESTS} concurrent requests...\n")

    # Threaded benchmark
    print("🧵 Threaded (requests) benchmark...")
    start = time.perf_counter()
    print("Running threaded benchmark for the selected asset...")
    thread_sizes = threaded_benchmark(url, headers, NUM_REQUESTS)
    thread_time = time.perf_counter() - start

    # Asyncio benchmark
    print("\n⚡ Asyncio (aiohttp) benchmark...")
    start = time.perf_counter()
    print("Running asyncio benchmark for the selected asset...")
    print("Running asyncio benchmark for the selected asset...")
    async_sizes = uvloop.run(async_benchmark(url, headers, NUM_REQUESTS))
    async_time = time.perf_counter() - start

    # Validation
    assert all(s == thread_sizes[0] for s in thread_sizes), "❌ Threaded sizes mismatch!"
    assert all(s == async_sizes[0] for s in async_sizes), "❌ Async sizes mismatch!"
    assert thread_sizes[0] == async_sizes[0], "❌ Size mismatch between thread/async!"

    # Report
    print("\n📊 Benchmark Results:")
    print(f"Threaded requests: {thread_time:.2f} seconds")
    print(f"Asyncio requests:  {async_time:.2f} seconds")
    print(f"Average speed (threads): {NUM_REQUESTS / thread_time:.2f} req/sec")
    print(f"Average speed (async):   {NUM_REQUESTS / async_time:.2f} req/sec")
    print(f"Performance difference: {abs(thread_time - async_time):.2f} seconds")
    print("🏁", "Threaded" if thread_time < async_time else "Asyncio", "approach was faster")

    # Output
    # 📊 Benchmark Results -> with uvloop 
    # Threaded requests: 0.37 seconds
    # Asyncio requests:  0.37 seconds
    # Average speed (threads): 27.30 req/sec
    # Average speed (async):   26.69 req/sec
    # Performance difference: 0.01 seconds
    # 🏁 Threaded approach was faster
    # 📊 Benchmark Results:
    # Threaded requests: 0.38 seconds
    # Asyncio requests:  0.38 seconds
    # Average speed (threads): 53.25 req/sec
    # Average speed (async):   52.73 req/sec
    # Performance difference: 0.00 seconds
    # 🏁 Threaded approach was faster
    # 
    # 📊 Benchmark Results:
    # Threaded requests: 0.41 seconds
    # Asyncio requests:  0.39 seconds
    # Average speed (threads): 48.28 req/sec
    # Average speed (async):   51.89 req/sec
    # Performance difference: 0.03 seconds
    # 🏁 Asyncio approach was faster


if __name__ == "__main__":
    run_benchmark()


### APPIMAGE BENCHMARK
#
# OUTPUT
# Threaded downloads: 13.78 seconds
# Asyncio downloads:  13.97 seconds
# Average speed (threaded): 0.22 downloads/sec
# Average speed (asyncio):  0.21 downloads/sec
# Performance difference: 0.19 seconds
# 🏁 Threaded approach was faster
#
# import os
# import time
# import asyncio
# import aiohttp
# import requests
# import tempfile
# from concurrent.futures import ThreadPoolExecutor

# # Configuration
# QOWNNOTES_REPO = "pbek/QOwnNotes"
# APPFLOWY_REPO = "AppFlowy-IO/AppFlowy"
# NUM_DOWNLOADS = 3

# def get_latest_appimage_url(repo):
#     """Fetch latest AppImage URL from a GitHub repo"""
#     url = f"https://api.github.com/repos/{repo}/releases/latest"
#     response = requests.get(url)
#     response.raise_for_status()

#     for asset in response.json()['assets']:
#         if asset['name'].endswith('.AppImage'):
#             return asset['browser_download_url']

#     raise ValueError(f"No AppImage found in latest release for {repo}")

# def download_file(url, path):
#     """Download a file synchronously"""
#     with requests.get(url, stream=True) as r:
#         r.raise_for_status()
#         with open(path, 'wb') as f:
#             for chunk in r.iter_content(chunk_size=8192):
#                 f.write(chunk)

# def download_worker(url, path):
#     """Thread worker for downloading files"""
#     download_file(url, path)

# async def async_download(session, url, path):
#     """Asynchronous file download using aiohttp"""
#     async with session.get(url) as response:
#         response.raise_for_status()
#         with open(path, 'wb') as f:
#             while True:
#                 chunk = await response.content.read(8192)
#                 if not chunk:
#                     break
#                 f.write(chunk)

# async def async_download_manager(url, num_downloads):
#     """Manage asynchronous downloads"""
#     async with aiohttp.ClientSession() as session:
#         tasks = []
#         paths = []
#         for _ in range(num_downloads):
#             fd, path = tempfile.mkstemp(suffix=".AppImage", prefix="async_")
#             os.close(fd)
#             paths.append(path)
#             tasks.append(async_download(session, url, path))
#         await asyncio.gather(*tasks)
#         return paths

# def thread_download(url, num_downloads):
#     """Download using thread pool"""
#     with ThreadPoolExecutor(max_workers=num_downloads) as executor:
#         paths = []
#         futures = []
#         for _ in range(num_downloads):
#             fd, path = tempfile.mkstemp(suffix=".AppImage", prefix="thread_")
#             os.close(fd)
#             paths.append(path)
#             futures.append(executor.submit(download_worker, url, path))
#         for future in futures:
#             future.result()
#         return paths

# def benchmark(url):
#     """Run and compare download methods"""
#     # Threaded benchmark
#     start = time.perf_counter()
#     thread_paths = thread_download(url, NUM_DOWNLOADS)
#     thread_time = time.perf_counter() - start

#     # Async benchmark
#     start = time.perf_counter()
#     async_paths = asyncio.run(async_download_manager(url, NUM_DOWNLOADS))
#     async_time = time.perf_counter() - start

#     # Size verification
#     all_paths = thread_paths + async_paths
#     sizes = [os.path.getsize(p) for p in all_paths]
#     if len(set(sizes)) != 1:
#         print("⚠️  Warning: Downloaded file sizes differ!")
#     else:
#         print("✅ All downloaded file sizes match.")

#     # Benchmark report
#     print(f"\nBenchmark Results ({NUM_DOWNLOADS} downloads each):")
#     print(f"Threaded downloads: {thread_time:.2f} seconds")
#     print(f"Asyncio downloads:  {async_time:.2f} seconds")
#     print(f"Average speed (threaded): {NUM_DOWNLOADS / thread_time:.2f} downloads/sec")
#     print(f"Average speed (asyncio):  {NUM_DOWNLOADS / async_time:.2f} downloads/sec")
#     print(f"Performance difference: {abs(thread_time - async_time):.2f} seconds")

#     if thread_time < async_time:
#         print("🏁 Threaded approach was faster")
#     else:
#         print("🏁 Asyncio approach was faster")

#     # Clean up
#     print("\nCleaning up temporary files...")
#     for p in all_paths:
#         if os.path.exists(p):
#             os.remove(p)

# def install_appimage(url, label):
#     """Download and make an AppImage executable"""
#     fd, temp_path = tempfile.mkstemp(suffix=".AppImage", prefix=f"{label}_")
#     os.close(fd)
#     print(f"Installing {label} AppImage...")
#     download_file(url, temp_path)
#     os.chmod(temp_path, 0o755)
#     print(f"{label} installed to {temp_path} (executable)")
#     return temp_path

# def main():
#     print("Fetching latest QOwnNotes release...")
#     qownnotes_url = get_latest_appimage_url(QOWNNOTES_REPO)
#     print(f"QOwnNotes URL: {qownnotes_url}")

#     print("Fetching latest AppFlowy release...")
#     appflowy_url = get_latest_appimage_url(APPFLOWY_REPO)
#     print(f"AppFlowy URL: {appflowy_url}")

#     # Install two AppImages
#     install_appimage(qownnotes_url, "QOwnNotes")
#     install_appimage(appflowy_url, "AppFlowy")

#     # Run benchmark
#     print("\nStarting download benchmarks...")
#     benchmark(qownnotes_url)

# if __name__ == "__main__":
#     main()
