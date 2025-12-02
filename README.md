# Antigravity Auto-Accept Macro

This tool automatically clicks the "Accept" button in the Antigravity terminal prompts.

## Setup

1.  **Capture the Button Image**:
    *   Wait for an Antigravity prompt to appear in VS Code.
    *   Use the "Snipping Tool" or `Win+Shift+S` to take a screenshot of **ONLY** the "Accept" button.
    *   Save this image as `accept.png` in this folder: `c:\Users\Administrator\Desktop\autoaccept antigravity macro`.
    *   **Important**: The image should contain only the button, not the surrounding background, for best results.

2.  **Run the Macro**:
    *   Double-click `run_macro.bat`.
    *   Or run `python auto_accept.py` in the terminal.

## Usage

*   The script will run in a loop and look for the button.
*   When it sees the button, it will click it.
*   To stop the macro, press `Ctrl+C` in the terminal window or move your mouse quickly to the top-left corner of the screen.
