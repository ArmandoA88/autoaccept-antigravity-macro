import pyautogui
import time
import os
import sys

# Fail-safe: moving mouse to upper-left corner will throw an exception and exit
pyautogui.FAILSAFE = True

def main():
    print("Auto-accept macro started.")
    print("Press Ctrl+C to stop in the terminal, or move mouse to upper-left corner.")
    
    image_filename = 'accept.png'
    
    if not os.path.exists(image_filename):
        print(f"Error: '{image_filename}' not found in the current directory.")
        print("Please take a screenshot of the 'Accept' button and save it as 'accept.png'.")
        print("Make sure to crop it tightly around the button.")
        input("Press Enter to exit...")
        return

    print(f"Looking for {image_filename}...")

    try:
        while True:
            try:
                # Locate the button on the screen
                # confidence=0.9 requires opencv-python to be installed
                # We use a high confidence to avoid false positives
                location = pyautogui.locateOnScreen(image_filename, confidence=0.8, grayscale=False)
                
                if location:
                    print(f"Button found at {location}. Clicking...")
                    center = pyautogui.center(location)
                    pyautogui.click(center)
                    # Move mouse back to original position? No, that might be annoying.
                    # Just sleep to allow the UI to update.
                    time.sleep(2) 
                else:
                    # Sleep briefly to save CPU
                    time.sleep(0.5)
            except pyautogui.ImageNotFoundException:
                # This exception is raised if the image is not found (in newer versions)
                time.sleep(0.5)
            except Exception as e:
                # print(f"Scanning... ({e})") # Debug
                time.sleep(0.5)
                
    except KeyboardInterrupt:
        print("\nMacro stopped by user.")

if __name__ == "__main__":
    main()
