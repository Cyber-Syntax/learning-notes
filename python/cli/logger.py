import asyncio
import logging
import os
import random
from logging.handlers import RotatingFileHandler

# -------------------------
# Logging setup (file + console + rotation)
# -------------------------
LOG_FILE = os.path.join(os.path.dirname(__file__), "async-app.log")

logger = logging.getLogger("async-downloader")
logger.setLevel(logging.INFO)

formatter = logging.Formatter("%(asctime)s | %(levelname)s | %(message)s")

# File handler with rotation (10 KB limit)
file_handler = RotatingFileHandler(
    LOG_FILE,
    maxBytes=10 * 1024,  # 10 KB
    backupCount=5,
)
file_handler.setFormatter(formatter)

# Console handler
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(console_handler)


# -------------------------
# Fake download
# -------------------------
async def fake_download(file_name: str, queue: asyncio.Queue):
    logger.info(f"[START DOWNLOAD] {file_name}")

    chunks = random.randint(5, 10)

    for i in range(1, chunks + 1):
        await asyncio.sleep(random.uniform(0.1, 0.4))
        logger.info(f"[DOWNLOADING] {file_name} chunk {i}/{chunks}")

    logger.info(f"[DOWNLOAD COMPLETE] {file_name}")

    await queue.put(file_name)


# -------------------------
# Fake extractor
# -------------------------
async def extractor_worker(queue: asyncio.Queue):
    while True:
        file_name = await queue.get()

        if file_name is None:
            break

        logger.info(f"[EXTRACT START] {file_name}")
        await asyncio.sleep(random.uniform(0.3, 1.0))
        logger.info(f"[EXTRACT DONE] {file_name}")

        queue.task_done()


# -------------------------
# Main
# -------------------------
async def main():
    queue = asyncio.Queue()

    files = [f"file_{i}.zip" for i in range(1, 8)]

    extractor_task = asyncio.create_task(extractor_worker(queue))

    download_tasks = [asyncio.create_task(fake_download(f, queue)) for f in files]

    await asyncio.gather(*download_tasks)

    await queue.join()

    await queue.put(None)
    await extractor_task

    logger.info("ALL DOWNLOADS + EXTRACTIONS COMPLETE")


if __name__ == "__main__":
    asyncio.run(main())
