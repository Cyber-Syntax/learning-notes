import time
import keyboard

def press_key(key, duration=0.2):
    keyboard.press(key)
    time.sleep(duration)
    keyboard.release(key)
    time.sleep(0.2)

def skill(number):
    press_key(str(number))

def move(direction, duration):
    press_key(direction, duration)

def canavar_sec():
    press_key('b', 0.4)

def duz_vur():
    press_key('r', 2)

def sutun2():
    press_key('F2')

time.sleep(3)
for i in range(10):
    canavar_sec()
    time.sleep(0.2)
    skill(4)
    time.sleep(0.2)
    skill(1)
    time.sleep(2)
    duz_vur()
    duz_vur()
    time.sleep(0.2)
