import pyautogui
print(11)
import time

box = pyautogui.locateOnScreen('5.png')

print(box.left, box.top)

while True:
    print(pyautogui.position())
    print(pyautogui.moveTo(box.left, box.top))

    
