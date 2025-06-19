import asyncio

import easyocr
import mss
import numpy as np
from PIL import Image
from thefuzz import fuzz

import server

BBOX = (2017, 1209, 2382, 1252)
TARGET_TEXTS = ["已得到恐怖强敌的所在地信息"]

DEBUG = False
backend = easyocr.Reader(["ch_sim"])


def ocr(img):
    return "".join(res[1] for res in backend.readtext(img))  # type: ignore


async def start():
    with mss.mss() as sct:
        while True:
            img = np.array(sct.grab(BBOX))
            if DEBUG:
                Image.fromarray(img).save("temp.png")
            recognized = ocr(img)
            if any(fuzz.ratio(recognized, target) > 80 for target in TARGET_TEXTS):
                print(recognized, "auto split")
                server.send_action("split")
                await asyncio.sleep(10)
            await asyncio.sleep(0.5)
