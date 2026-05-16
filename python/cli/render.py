import asyncio

downloads = {
    "obsidian": 45,
    "appflowy": 82,
}


async def download(pkg):
    for progress in range(101):
        downloads[pkg] = progress
        await asyncio.sleep(0.1)


async def renderer():
    while True:
        print("\033c", end="")  # clear screen

        for pkg, progress in downloads.items():
            print(f"{pkg}: {progress}%")

        await asyncio.sleep(0.2)


if __name__ == "__main__":
    download("obsidian")
