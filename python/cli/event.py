"""Workers NEVER print directly.

workers emit events
renderer prints events
"""

import asyncio
from dataclasses import dataclass
from enum import Enum, auto


class Event(Enum):
    DOWNLOAD_STARTED = auto()
    DOWNLOAD_FINISHED = auto()

    APPIMAGE_VERIFIED = auto()
    APPIMAGE_VERIFICATION_SKIPPED = auto()

    APPIMAGE_INSTALLED = auto()
    APPIMAGE_FAILED = auto()


@dataclass
class PackageEvent:
    event: Event
    package: str
    message: str = ""


queue = asyncio.Queue()


async def downloader():
    await queue.put(PackageEvent(Event.DOWNLOAD_STARTED, "obsidian"))

    await asyncio.sleep(1)

    await queue.put(PackageEvent(Event.DOWNLOAD_FINISHED, "obsidian"))


async def renderer():
    while True:
        event = await queue.get()

        print(event)


async def main():
    asyncio.create_task(renderer())
    await downloader()


asyncio.run(main())
