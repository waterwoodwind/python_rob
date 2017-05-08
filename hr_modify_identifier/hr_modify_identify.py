import pyautogui
import pyperclip
import time

pyautogui.PAUSE = 2.0
pyautogui.FAILSAFE = False

def modify():
    time.sleep(4)
    pyautogui.hotkey('ctrl', 'e')
    time.sleep(5)
    pyautogui.click(50, 370)
    pyautogui.moveTo(125,400)
    pyautogui.click(clicks=2)
    pyautogui.hotkey('ctrl', 'c')
    id_number = pyperclip.paste()
    last_5_number = id_number[5:10]
    new_id_number = "8003" + last_5_number + "8"
    print new_id_number
    pyperclip.copy(new_id_number)
    time.sleep(2)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(1)
    pyautogui.click(125,380)
    pyautogui.click(125,400, clicks=2)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.hotkey('ctrl', 's')
    time.sleep(10)
    pyautogui.click(1450, 340)

for i in range(55):
    modify()
