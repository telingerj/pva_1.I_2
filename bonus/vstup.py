import pyautogui
import time

time.sleep(2)
#print(pyautogui.position())
pyautogui.moveTo(1248, 1179, duration=1)
pyautogui.click()
pyautogui.write("ahoj", interval=1)
pyautogui.press("enter")
