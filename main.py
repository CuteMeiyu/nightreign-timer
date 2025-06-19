import asyncio

import server
import splits.hotkey
import splits.ocr


async def main():
    await asyncio.gather(
        splits.hotkey.start(),
        splits.ocr.start(),
        server.start(),
    )


asyncio.run(main())
