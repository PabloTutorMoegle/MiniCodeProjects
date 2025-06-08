import pyautogui as py
import keyboard

position = (960, 606)

while True:
    if keyboard.read_key() == 'p':
        for i in range(9):
            for i in range(36000):
                py.click(position)
