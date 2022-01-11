import pyautogui
import time

def seemta():
    im = pyautogui.screenshot()
    im.save('image.png')
    acc = pyautogui.locateOnScreen('see.png', confidence=0.9)
    acc_co = pyautogui.center(acc)
    x, y = acc_co.x, acc_co.y
    pyautogui.moveTo(x, y)
    pyautogui.click(x, y)
    pyautogui.moveTo(877, 770, 2)

for i in range(3):
    seemta()
    time.sleep(10)
