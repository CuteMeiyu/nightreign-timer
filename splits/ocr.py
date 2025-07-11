import asyncio

import server

TARGETS = [
    {
        "rect": (0.4152, 0.4979, 0.5832, 0.5861),
        "texts": ["DAY I", "DAY II"],
        "threshold": 70,
        "action": "split",
        "cooldown": 30,
    },
    {
        "rect": (0.7879, 0.8396, 0.9305, 0.8694),
        "texts": ["已得到恐怖强敌的所在地信息"],
        "threshold": 70,
        "action": "split",
        "cooldown": 30,
    },
    {
        "rect": (0.8578, 0.0917, 0.9641, 0.1250),
        "texts": ["已完成出击的准备"],
        "threshold": 70,
        "action": "reset",
        "cooldown": 10,
    },
]
MONITOR = 1  # Monitor index, starting with 1. https://python-mss.readthedocs.io/api.html#mss.tools.mss.base.MSSBase.monitors
INTERVAL = 0.6  # Interval between twice detection


async def start():
    import easyocr
    import mss
    import numpy as np
    from PIL import Image
    from thefuzz import fuzz

    reader = easyocr.Reader(["ch_sim", "en"])

    def get_screen_size():
        screenshot = sct.grab(sct.monitors[MONITOR])
        # return 1920, 1080
        return screenshot.width, screenshot.height

    def grab(bbox):
        # return np.array(Image.open("screenshot.png"))[bbox[1] : bbox[3], bbox[0] : bbox[2]]
        return np.array(sct.grab(bbox))

    def ocr(img):
        return " ".join(res[1] for res in reader.readtext(img))  # type: ignore

    with mss.mss() as sct:
        width, height = get_screen_size()
        for target in TARGETS:
            target["bbox"] = (
                int(width * target["rect"][0]),
                int(height * target["rect"][1]),
                int(width * target["rect"][2]),
                int(height * target["rect"][3]),
            )
        interval = INTERVAL / len(TARGETS)
        print("ocr ready")
        while True:
            for i, target in enumerate(TARGETS):
                img = grab(target["bbox"])
                recognized = ocr(img)
                # Image.fromarray(img).save(f"temp-{i}.png")
                # print(recognized)
                if any((ratio := fuzz.ratio(recognized, text)) >= target["threshold"] for text in target["texts"]):
                    print(recognized, ratio, target["action"])
                    server.send_action(target["action"])
                    await asyncio.sleep(target["cooldown"])
                await asyncio.sleep(interval)


if __name__ == "__main__":
    asyncio.run(start())
