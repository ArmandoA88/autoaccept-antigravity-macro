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

    last_location = None

    try:
        while True:
            try:
                location = None
                
                # 1. OPTIMIZATION: Smart Search
                if last_location:
                    x, y, w, h = last_location
                    region = (max(0, x - 50), max(0, y - 50), w + 100, h + 100)
                    try:
                        # Increased confidence to 0.9 and enabled color matching (grayscale=False)
                        # This prevents clicking "Main" or "Commit" buttons which look similar in shape but different in color/text
                        location = pyautogui.locateOnScreen(image_filename, region=region, confidence=0.75, grayscale=False)
                    except pyautogui.ImageNotFoundException:
                        pass 

                # 2. Full Screen Search
                if not location:
                    # High confidence + Color matching is crucial to avoid false positives
                    location = pyautogui.locateOnScreen(image_filename, confidence=0.75, grayscale=False)
                
                if location:
                    print(f"[{time.strftime('%H:%M:%S')}] Button found at {location}. Clicking...")
                    center = pyautogui.center(location)
                    pyautogui.click(center)
                    last_location = location
                    time.sleep(2) 
                else:
                    time.sleep(0.5)

            except pyautogui.ImageNotFoundException:
                time.sleep(0.5)
            except Exception as e:
                print(f"Scanning error: {e}")
                time.sleep(0.5)
                
    except KeyboardInterrupt:
        print("\nMacro stopped by user.")

if __name__ == "__main__":
    main()
