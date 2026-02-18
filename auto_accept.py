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
    target_images = ['accept.png', 'run.png', 'submit.png']
    
    # Check if at least one image exists
    existing_images = [img for img in target_images if os.path.exists(img)]
    if not existing_images:
        print(f"Error: No target images found (looked for {target_images}).")
        print("Please save 'accept.png', 'run.png', and/or 'submit.png' in this folder.")
        # Instructions for the user
        print("\nTo fix this:")
        print("1. Take a screenshot of the button you want to auto-click.")
        print("2. Save it as 'accept.png' or 'run.png' in this folder.")
        input("Press Enter to exit...")
        return

    print(f"Looking for: {', '.join(existing_images)}...")

    # Dictionary to store the last known location for EACH image
    last_locations = {}

    try:
        while True:
            try:
                location = None
                found_image = None
                
                # 1. OPTIMIZATION: Smart Search (Check last known location for each image first)
                for img_name in existing_images:
                    if img_name in last_locations:
                        x, y, w, h = last_locations[img_name]
                        # Create a region around the last known location
                        # Expanded region to be safe
                        region = (max(0, x - 50), max(0, y - 50), w + 100, h + 100)
                        try:
                            # Search only in that region
                            # Lowered confidence slightly to 0.7 to ensure detection
                            location = pyautogui.locateOnScreen(img_name, region=region, confidence=0.7, grayscale=False)
                            if location:
                                found_image = img_name
                                break
                        except pyautogui.ImageNotFoundException:
                            # If not found in the old spot, remove it from memory so we search full screen next time
                            del last_locations[img_name]
                            pass 
                
                # 2. Full Screen Search (if not found in last location)
                if not location:
                    for img_name in existing_images:
                        try:
                            # Lowered confidence to 0.7 for better detection
                            location = pyautogui.locateOnScreen(img_name, confidence=0.7, grayscale=False)
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
                    
                    # Update the last known location for THIS specific image
                    last_locations[found_image] = location
                    
                    time.sleep(2) 
                else:
                    # Button not found. Check for anchor to scroll down.
                    anchor_filename = 'anchor.png'
                    if os.path.exists(anchor_filename):
                        try:
                            anchor_loc = pyautogui.locateOnScreen(anchor_filename, confidence=0.7, grayscale=False)
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
