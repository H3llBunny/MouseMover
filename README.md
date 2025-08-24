# Auto Mouse Mover

A simple Python tool that prevents your computer from going idle by automatically moving the mouse and scrolling when idle.  
You can stop it anytime with **CTRL+ALT+Q** or by closing the terminal.

---

## 🚀 How to Use
### Option 1: Download the `.exe`
1. Download the prebuilt **`mouse.exe`** from [![Release](https://img.shields.io/badge/release-v1.0-blue)](https://github.com/H3llBunny/MouseMover/releases/tag/v1.0.0)
2. Double-click to run.  
3. The script will:
   - Detect if your mouse is idle
   - Randomly move it within a defined range
   - Scroll slightly  
4. Quit anytime with **CTRL+ALT+Q**.

---

### Option 2: Run from Source
1. Install [Python 3](https://www.python.org/downloads/).  
2. Clone this repo:
   ```bash
   git clone https://github.com/H3llBunny/MouseMover.git
   cd MouseMover
3. Install dependencies:
   ```bash
   pip install pyautogui keyboard
4. Run:
   ```bash
   python mouse.py

---

### Option 3: Build Your Own `.exe`
1. Install PyInstaller:
   ```bash
   pip install pyinstaller
2. Build the `.exe`:
   ```bash
   pyinstaller --onefile mouse.py
3. The `.exe` will be created inside the `dist/` folder.

📝 Notes

Default idle threshold = 20 seconds (you can change this in the code).

Hotkey to quit = CTRL+ALT+Q.

Coordinates (2500–2600, 800–900) may need adjusting for your monitor setup.
