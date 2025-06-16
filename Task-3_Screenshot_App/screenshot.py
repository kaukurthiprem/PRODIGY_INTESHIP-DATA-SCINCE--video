import pyautogui
import time

filename = input("Enter filename (e.g., image.png): ")
time.sleep(3)
screenshot = pyautogui.screenshot()
screenshot.save(filename)
print(f"Screenshot saved as {filename}")