import pyautogui
import time
import os
import sys

def setup_button_image():
    print("--- Auto-Accept Macro Setup ---")
    print("This setup will help you capture the 'Accept' button image correctly.")
    print("\n1. Open the window where the 'Accept' button is visible.")
    print("2. Move your mouse cursor to the CENTER of the 'Accept' button.")
    print("3. Keep the mouse still.")
    
    input("\nPress ENTER when your mouse is positioned over the button...")
    
    # Get mouse position
    x, y = pyautogui.position()
    print(f"Capturing button at ({x}, {y})...")
    
    # Capture a small region around the mouse. 
    # Buttons are usually around 100-150px wide and 30-40px tall.
    # Let's capture a safe 60x30 region centered on the mouse to get the unique text/icon part.
    # We don't need the whole button, just a unique part of it.
    width = 60
    height = 30
    left = int(x - width/2)
    top = int(y - height/2)
    
    try:
        # Capture screenshot
        screenshot = pyautogui.screenshot(region=(left, top, width, height))
        
        # Save it
        filename = 'accept.png'
        screenshot.save(filename)
        print(f"\nSaved '{filename}'.")
        
        # Verify
        print("Verifying if we can find the new image...")
        time.sleep(0.5)
        try:
            location = pyautogui.locateOnScreen(filename, confidence=0.7)
            if location:
                print("SUCCESS! The button was detected.")
                print("You can now run 'run_macro.bat'.")
            else:
                print("WARNING: Could not detect the image immediately. It might be too generic.")
                print("Try running this setup again, but capture a slightly different part of the button.")
        except Exception as e:
            print(f"Verification failed: {e}")
            
    except Exception as e:
        print(f"Error capturing screenshot: {e}")

if __name__ == "__main__":
    setup_button_image()
