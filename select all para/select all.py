import autopy
import time


autopy.mouse.move(261,362)
time.sleep(2)

for i in range(1,1600):
    autopy.mouse.click()
    time.sleep(1)
    autopy.key.tap(autopy.key.K_DOWN)
    time.sleep(1)

