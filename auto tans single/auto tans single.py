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

autopy.mouse.move(400,400)
time.sleep(1)
autopy.mouse.click()
time.sleep(1)
autopy.key.tap('d',autopy.key.MOD_CONTROL)
#autopy.key.toggle('f',True, autopy.key.MOD_CONTROL)
#autopy.key.toggle('f',False, autopy.key.K_CONTROL)
time.sleep(1)
path = u'F:\微云同步盘\9.资源\译码研究\B-1763_20150831014747.wgl'
#path = path.encode('gbk')
setText(path)
autopy.key.tap('v',autopy.key.MOD_CONTROL)
autopy.key.tap(9)
autopy.key.tap(9)
autopy.key.tap(autopy.key.K_DOWN)
autopy.key.tap(9)
autopy.key.tap(autopy.key.K_RETURN)
tailnumber = u'B1774'
setText(tailnumber)
autopy.key.tap('v',autopy.key.MOD_CONTROL)
#autopy.key.tap(autopy.key.K_RETURN)