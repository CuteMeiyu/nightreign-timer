import asyncio
import time

import easyocr
import keyboard
import mss
import numpy as np
from thefuzz import fuzz

import server

HOTKEYS = {
    "1": "split",
    "2": "next",
    "3": "reset",
    "8": "prev",
}

ocr = easyocr.Reader(["ch_sim"]).readtext


async def enemy_hint_detection():
    bbox = (2017, 1209, 2382, 1252)
    with mss.mss() as sct:
        while True:
            img = np.array(sct.grab(bbox))
            result = ocr(img)
            text = "".join([res[1] for res in result])  # type: ignore
            if fuzz.ratio(text, "已得到恐怖强敌的所在地信息") > 80:
                print("Enemy hint detected, sending split action.")
                server.send_action("split")
                await asyncio.sleep(10)
            await asyncio.sleep(0.5)


async def main():
    for hotkey, action in HOTKEYS.items():
        keyboard.add_hotkey(hotkey, server.send_action, (action,))
    await asyncio.gather(
        enemy_hint_detection(),
        server.start(),
    )


asyncio.run(main())
