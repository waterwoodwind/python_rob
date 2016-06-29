#coding=utf-8
import pyautogui

number_locate = pyautogui.locateCenterOnScreen('com_box.png')
print number_locate
print type(number_locate)
pyautogui.moveTo(number_locate)
pyautogui.click()