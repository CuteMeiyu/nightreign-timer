import keyboard

import server

HOTKEYS = {
    "1": "split",
    "2": "next",
    "3": "reset",
    "8": "prev",
}

for hotkey, action in HOTKEYS.items():
    keyboard.add_hotkey(hotkey, server.send_action, (action,))


async def start():
    pass
