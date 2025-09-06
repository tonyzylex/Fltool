import pyautogui
import time

print("Move your mouse to the input box within 5 seconds...")
time.sleep(5)
print(pyautogui.position())  # shows (x, y) of your mouse