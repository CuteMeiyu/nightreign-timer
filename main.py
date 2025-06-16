import asyncio

import keyboard

import server

HOTKEYS = {
    "1": "split",
    "2": "next",
    "3": "reset",
    "8": "prev",
}


async def main():
    for hotkey, action in HOTKEYS.items():
        keyboard.add_hotkey(hotkey, server.send_action, (action,))
    await server.start()


asyncio.run(main())
