# Elden Ring Nightreign Timer

## Usage

- Open index.html / Add browser source in OBS
- run main.py
- press "1" while "DAY I"/"DAY II" appearing

## Hotkey

- 1: Split (go to next phase with retiming)
- 2: Go to next phase
- 3: Reset
- 4: Undo split
- 5: Back to previous phase
- Custom config in splits/hotkey.py

## AutoTimer

- Based on OCR ([EasyOCR](https://github.com/JaidedAI/EasyOCR))
- Detect "DAY I"/"DAY II" on center of screen
- Additionally detect great enemy tip on day 2, as a backup when map opened (Chinese only)
- Custom config in splits/ocr.py
- Only tests on 16:9 aspect ratio
- Can be disabled by commenting out `splits.ocr.start()` in the main.py

## Remote Display

- Open index.html
- Right click to config host ip address
