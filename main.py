import pyautogui
import time
import random
import sys
import keyboard

def left():
    pyautogui.press('left')

def right():
    pyautogui.press('right')

def up():
    pyautogui.press('up')

def down():
    pyautogui.press('down')

def first_type():
    i = 1
    while i <= 10000000:
        if keyboard.is_pressed('q'):  # if key 'q' is pressed
            sys.exit()
        down()
        left()
        up()
        right()

def second_type():
    i = 1
    while i <= 10000000:
        if keyboard.is_pressed('q'):  # if key 'q' is pressed
            sys.exit()
        selection1 = random.randint(0,3)
        if selection1 == 0:
            left()
        elif selection1 == 1:
            right()
        elif selection1 == 2:
            up()
        elif selection1 == 3:
            down()

selection = input("Выберите тип игры: первый, или второй")
time.sleep(2)

if selection == "первый":
    first_type()
elif selection == "второй":
    second_type()
