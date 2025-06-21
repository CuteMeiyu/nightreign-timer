import asyncio

import server

HOTKEYS = {
    "1": "split",
    "2": "next",
    "3": "reset",
    "4": "undo",
    "5": "prev",
}


async def start():
    import keyboard

    for hotkey, action in HOTKEYS.items():
        keyboard.add_hotkey(hotkey, server.send_action, (action,))
    print("hotkey ready")
    while True:
        await asyncio.sleep(1e6)
