import pyautogui
import time
import os
import sys

# Fail-safe: moving mouse to upper-left corner will throw an exception and exit
pyautogui.FAILSAFE = True

def main():
    print("Auto-accept macro started.")
    print("Press Ctrl+C to stop in the terminal, or move mouse to upper-left corner.")
    
    # List of images to search for
    target_images = ['accept.png', 'run.png']
    
    # Check if at least one image exists
    existing_images = [img for img in target_images if os.path.exists(img)]
    if not existing_images:
        print(f"Error: No target images found (looked for {target_images}).")
        print("Please save 'accept.png' and/or 'run.png' in this folder.")
        # Instructions for the user
        print("\nTo fix this:")
        print("1. Take a screenshot of the button you want to auto-click.")
        print("2. Save it as 'accept.png' or 'run.png' in this folder.")
        input("Press Enter to exit...")
        return

    print(f"Looking for: {', '.join(existing_images)}...")

    last_location = None

    try:
        while True:
            try:
                location = None
                found_image = None
                
                # 1. OPTIMIZATION: Smart Search (Check last known location first)
                if last_location:
                    x, y, w, h = last_location
                    region = (max(0, x - 50), max(0, y - 50), w + 100, h + 100)
                    try:
                        for img_name in existing_images:
                            location = pyautogui.locateOnScreen(img_name, region=region, confidence=0.75, grayscale=False)
                            if location:
                                found_image = img_name
                                break
                    except pyautogui.ImageNotFoundException:
                        pass 
                
                # 2. Full Screen Search
                if not location:
                    for img_name in existing_images:
                        try:
                            # High confidence + Color matching is crucial to avoid false positives
                            location = pyautogui.locateOnScreen(img_name, confidence=0.75, grayscale=False)
                            if location:
                                found_image = img_name
                                break
                        except pyautogui.ImageNotFoundException:
                            pass
                
                if location:
                    print(f"[{time.strftime('%H:%M:%S')}] Found '{found_image}' at {location}. Clicking...")
                    
                    # Save current mouse position
                    current_mouse_x, current_mouse_y = pyautogui.position()
                    
                    center = pyautogui.center(location)
                    pyautogui.click(center)
                    
                    # Restore mouse position
                    pyautogui.moveTo(current_mouse_x, current_mouse_y)
                    
                    last_location = location
                    time.sleep(2) 
                else:
                    # Button not found. Check for anchor to scroll down.
                    anchor_filename = 'anchor.png'
                    if os.path.exists(anchor_filename):
                        try:
                            anchor_loc = pyautogui.locateOnScreen(anchor_filename, confidence=0.75, grayscale=False)
                            if anchor_loc:
                                print(f"[{time.strftime('%H:%M:%S')}] Anchor found. Scrolling down...")
                                # Move mouse below the anchor (header) to ensure we are over the content
                                target_x = anchor_loc.left + (anchor_loc.width // 2)
                                target_y = anchor_loc.top + anchor_loc.height + 100 # 100px below anchor
                                
                                # Save current mouse position
                                current_mouse_x, current_mouse_y = pyautogui.position()
                                
                                pyautogui.moveTo(target_x, target_y)
                                pyautogui.scroll(-1000) # Scroll down more (negative is down on Windows)
                                
                                # Restore mouse position
                                pyautogui.moveTo(current_mouse_x, current_mouse_y)
                                
                                time.sleep(1) # Wait a bit after scrolling before searching again
                        except pyautogui.ImageNotFoundException:
                            pass
                        except Exception as e:
                            print(f"Scroll error: {e}")

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
