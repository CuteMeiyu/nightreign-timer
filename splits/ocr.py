import asyncio

import server

TARGETS = [
    {
        "rect": (0.4152, 0.4979, 0.5832, 0.5861),
        "texts": ["DAY I", "DAY II"],
        "threshold": 50,
    },
    {
        "rect": (0.7879, 0.8396, 0.9305, 0.8694),
        "texts": ["已得到恐怖强敌的所在地信息"],
        "threshold": 70,
    },
]
DEBUG = False  # Save temp images
MONITOR = 1  # Monitor index, starting with 1. https://python-mss.readthedocs.io/api.html#mss.tools.mss.base.MSSBase.monitors
INTERVAL = 0.5  # Interval between twice detection
COOLDOWN = 30  # Cooldown after split


async def start():
    import easyocr
    import mss
    import numpy as np
    from PIL import Image
    from thefuzz import fuzz

    reader = easyocr.Reader(["ch_sim", "en"])

    def ocr(img):
        return " ".join(res[1] for res in reader.readtext(img))  # type: ignore

    with mss.mss() as sct:
        screenshot = sct.grab(sct.monitors[MONITOR])
        if DEBUG:
            Image.fromarray(np.array(screenshot)).save("screenshot.png")
        for target in TARGETS:
            target["bbox"] = (
                int(screenshot.width * target["rect"][0]),
                int(screenshot.height * target["rect"][1]),
                int(screenshot.width * target["rect"][2]),
                int(screenshot.height * target["rect"][3]),
            )
        interval = INTERVAL / len(TARGETS)
        print("ocr ready")
        while True:
            for i, target in enumerate(TARGETS):
                img = np.array(sct.grab(target["bbox"]))
                if DEBUG:
                    Image.fromarray(img).save(f"temp-{i}.png")
                recognized = ocr(img)
                if any(fuzz.ratio(recognized, text) >= target["threshold"] for text in target["texts"]):
                    print(recognized)
                    server.send_action("split")
                    await asyncio.sleep(COOLDOWN)
                await asyncio.sleep(interval)
