#coding: UTF-8
import autopy
import time
import sys
import os.path
import win32clipboard as w
import win32con


def setText(aString):
    w.OpenClipboard()
    w.EmptyClipboard()
    w.SetClipboardData(win32con.CF_UNICODETEXT, aString)
    w.CloseClipboard()

class AUTO():
    def auto_tran(self, loc_path, tail_number, file_name):
        autopy.mouse.move(400,400)
        time.sleep(1)
        autopy.mouse.click()
        time.sleep(1)
        autopy.key.tap('d',autopy.key.MOD_CONTROL)
        #autopy.key.toggle('f',True, autopy.key.MOD_CONTROL)
        #autopy.key.toggle('f',False, autopy.key.K_CONTROL)
        time.sleep(1)
        setText(loc_path)
        autopy.key.tap('v',autopy.key.MOD_CONTROL)
        autopy.key.tap(9)
        autopy.key.tap(9)
        autopy.key.tap(autopy.key.K_DOWN)
        autopy.key.tap(9)
        autopy.key.tap(autopy.key.K_RETURN)
        time.sleep(2)

        setText(tail_number)
        time.sleep(2)
        autopy.key.tap('v',autopy.key.MOD_CONTROL)
        autopy.key.tap(autopy.key.K_RETURN)
        time.sleep(2)
        newfilename = file_name + u".raw"
        print newfilename
        setText(newfilename)
        autopy.key.tap('v',autopy.key.MOD_CONTROL)
        #最后点确定
        time.sleep(0.5)
        autopy.key.tap(autopy.key.K_RETURN)
        time.sleep(0.5)
        autopy.key.tap(autopy.key.K_ESCAPE)
        #等待转录过程
        time.sleep(3)
        autopy.key.tap(autopy.key.K_RETURN)
