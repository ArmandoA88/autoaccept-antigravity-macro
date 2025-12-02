# 🚀 Antigravity Auto-Accept Macro

This tool automates the process of clicking the "Accept" button in Antigravity terminal prompts, saving you from repetitive clicking. It now includes smart auto-scrolling to find buttons that are off-screen.

---

## 📋 Features
- **Auto-Click**: Instantly detects and clicks the "Accept" button.
- **Smart Scroll**: Automatically scrolls down if the button is hidden (requires `anchor.png`).
- **Fail-Safe**: Move your mouse to the top-left corner of the screen to instantly stop the script.

---

## 🛠️ Setup Guide

### 1. Essential: The Button Image
The script needs to know what to look for.
1.  Wait for an Antigravity prompt to appear.
2.  Use **Snipping Tool** (`Win+Shift+S`) to capture **ONLY** the "Accept" button.
3.  Save it as `accept.png` in this folder.
    *   *Tip: Crop it tightly around the text/button edges. Avoid including the changing background.*

### 2. Optional: Auto-Scroll (New!)
If the "Accept" button is often hidden at the bottom of the list:
1.  Take a screenshot of a **static** part of the window header (e.g., the "Antigravity" title bar or a top icon).
2.  Save it as `anchor.png` in this folder.
3.  The script will now detect this header and scroll down automatically when it can't find the button.

---

## ▶️ How to Run
- **Double-click** `run_macro.bat` to start.
- **OR** run via terminal: `python auto_accept.py`

To **STOP** the macro:
- Press `Ctrl+C` in the terminal window.
- **OR** slam your mouse cursor into the **top-left corner** of your screen.

---

## ⚡ Auto-Start on Windows Boot
Want the macro to start automatically when you turn on your computer?

1.  **Open Startup Folder**:
    *   Press `Win + R` on your keyboard.
    *   Type `shell:startup` and press **Enter**.
2.  **Create Shortcut**:
    *   **Option A (Silent - Recommended)**: Right-click `run_silent.vbs` in this folder -> **Create shortcut**. Drag the shortcut into the Startup folder. This runs in the background with no window.
    *   **Option B (Visible)**: Right-click `run_macro.bat` -> **Create shortcut**. Drag it into the Startup folder. This keeps a terminal window open.
3.  **Done!** The macro will now launch every time you log in.

---

## 🔄 Recent Updates
- **v1.1**: Added **Auto-Scroll**. If `accept.png` is not found, the script looks for `anchor.png` and scrolls down 1000px to reveal hidden buttons.

---

## 💡 Troubleshooting
- **Not clicking?** Try taking a new screenshot of `accept.png`. Ensure your screen scaling hasn't changed.
- **Not scrolling?** Ensure `anchor.png` is visible on screen and matches the current window header.
