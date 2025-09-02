# Benchmark results:
# requests.get: 20 calls took 2.63 seconds
# aiohttp: 20 concurrent calls took 0.15 seconds

import time
import asyncio
import aiohttp
import requests

# GITHUB_API_URL = "https://api.github.com/repos/AppFlowy-IO/AppFlowy/releases/latest"
GITHUB_API_URL = "https://api.github.com/repos/pbek/QOwnNotes/releases/latest"


def benchmark_requests(n: int):
    start = time.time()
    for _ in range(n):
        resp = requests.get(GITHUB_API_URL)
        resp.raise_for_status()
        _ = resp.json()
    end = time.time()
    print(f"requests.get: {n} calls took {end - start:.2f} seconds")


async def fetch_aiohttp(session, url):
    async with session.get(url) as resp:
        resp.raise_for_status()
        return await resp.json()


async def benchmark_aiohttp(n: int):
    async with aiohttp.ClientSession() as session:
        start = time.time()
        tasks = [fetch_aiohttp(session, GITHUB_API_URL) for _ in range(n)]
        await asyncio.gather(*tasks)
        end = time.time()
        print(f"aiohttp: {n} concurrent calls took {end - start:.2f} seconds")


if __name__ == "__main__":
    n = 10  # number of API calls to benchmark
    benchmark_requests(n)
    asyncio.run(benchmark_aiohttp(n))
