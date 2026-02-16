# 🚀 Antigravity Auto-Accept Macro

This tool automates the process of clicking the "Accept" button in Antigravity terminal prompts. It runs quietly in the background and watches for the "Accept" prompt to appear on your screen.

## ✨ Features
- **Auto-Install**: Automatically installs all required Python libraries.
- **Smart Detection**: Uses advanced recognition to find the button even if it moved slightly.
- **Fail-Safe**: Move your mouse to the **top-left corner** of the screen to instantly kill the program.
- **Auto-Scroll**: Scrolls down if the button is hidden off-screen (requires `anchor.png`).

---

## 🛠️ Quick Setup (First Time Only)

1.  **Double-click `run_setup.bat`**.
    - This will install any missing files for you.
    - It will guide you to capture the "Accept" button image.
    - *Follow the on-screen instructions!*

2.  *(Optional)* **Auto-Start on Login**:
    - **Double-click `add_to_startup.bat`**.
    - This will automatically create a shortcut so the macro runs every time you start your computer.

---

## ▶️ Common Usage

### Start the Macro
Double-click **`run_macro.bat`**.
- A black window will appear showing "Looking for accept.png...".
- **Leave this window open** (you can minimize it).

### Stop the Macro
- Click inside the black window and press `Ctrl+C`.
- OR slam your mouse cursor into the **top-left corner** of your screen.

---

## ❓ Troubleshooting

**"The window opens and closes immediately"**
- We fixed this! The new script stays open and tells you exactly what went wrong. Read the error message in the window.

**"It says Python is not recognized"**
- You need to install Python. Download it from python.org and check the box **"Add Python to PATH"** during installation.

**"It's not clicking the button"**
- Your `accept.png` might be outdated or low quality.
- Run `run_setup.bat` again to capture a fresh image.
- Ensure the image is a **small, tight crop** of just the button text and color.

---

## 📂 Advanced Helper Files
- `auto_accept.py`: The main brain of the operation.
- `run_silent.vbs`: Run this if you want the macro to be **invisible** (no black window).
- `requirements.txt`: List of technical dependencies.
