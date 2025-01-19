import pyautogui as pt
import time

limit = int(input("Enter limit : "))
mssg = input("Enter Message : ")
i = 0
time.sleep(3)
while i < limit:
    pt.typewrite(mssg)
    pt.press("enter")
    i += 1
