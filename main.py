import asyncio

import server
import splits.hotkey
import splits.ocr


async def main():
    await asyncio.gather(
        server.start(),
        splits.hotkey.start(),
        splits.ocr.start(),
    )


asyncio.run(main())
