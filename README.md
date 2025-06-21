# Elden Ring Nightreign Timer

## Usage

- Open index.html / Add browser source in OBS
- run main.py
- press "1" while "DAY I"/"DAY II" appearing

## Hotkey

- 1: Go to next phase with retiming (start)
- 2: Go to next phase
- 3: Reset
- 4: Undo last split
- 5: Back to previous phase
- Custom config in splits/hotkey.py

## AutoTimer

- Based on OCR ([EasyOCR](https://github.com/JaidedAI/EasyOCR))
- Detect "DAY I"/"DAY II" on center of screen
- Additionally detect great enemy tip on day 2, as a backup when map opened (Chinese only)
- Custom config in splits/ocr.py
- Can be disabled by commenting out `splits.ocr.start()` in the main.py

## Remote

- Open index.html
- Right click to config host ip address
