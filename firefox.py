import pyautogui
import time

while True:
    im = pyautogui.screenshot()
    im.save('image.png')
    acc = pyautogui.locateOnScreen('see.png', confidence=0.9)
    acc_co = pyautogui.center(acc)
    x, y = acc_co.x, acc_co.y
    pyautogui.moveTo(x, y)
    pyautogui.click(x, y)
