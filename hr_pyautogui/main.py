#coding=utf-8
import pyautogui
import time

def put_a_day(human_number):
    pyautogui.PAUSE = 1
    number_locate = pyautogui.locateCenterOnScreen('number.png')
    pyautogui.moveTo(number_locate)
    pyautogui.click()

    pyautogui.typewrite(human_number, interval=0.25)
    query_locate = pyautogui.locateCenterOnScreen('query.png')
    pyautogui.moveTo(query_locate)
    pyautogui.click()

    com_box_locate = pyautogui.locateCenterOnScreen('com_box.png')
    pyautogui.moveTo(com_box_locate)
    pyautogui.click()

    chose_locate = pyautogui.locateCenterOnScreen('chose.png')
    pyautogui.moveTo(chose_locate)
    pyautogui.click()
    pyautogui.keyDown('pagedown')
    pyautogui.keyUp('pagedown')

f = open(u"人事.txt", "r")

time.sleep(5)
while True:
    line = f.readline()
    if line:
        human_number = line.strip('\n')
        put_a_day(human_number)
        pass    # do something here
    else:
        break
f.close()