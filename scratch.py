import msvcrt
import sys
import time
from pyautogui import *

while True:
    if msvcrt.kbhit():
        ch=msvcrt.getch()
        if ch==b'\x00' or ch==b'\xe0':
            ch=msvcrt.getch()
        if(ch==b'\x1b'):
            sys.exit()
        print(ch)
        if ch==b'i':
            moveTo(683, 384, 0)
            click(683, 384)


            keyDown('W')
            time.sleep(5)

            moveTo(1184, 384, 0)
            click()
        if ch==b'k':
            moveTo(683, 384, 0)
            click()
            press('s')
            moveTo(1184, 384, 0)
            click()
        if ch==b'j':
            moveTo(683, 384, 0)
            click()
            press('a')
            moveTo(1184, 384, 0)
            click()
        if ch==b'l':
            moveTo(683, 384, 0)
            click()
            press('d')
            moveTo(1184, 384, 0)
            click()



