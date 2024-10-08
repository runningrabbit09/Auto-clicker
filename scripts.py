# import modules
from pynput import keyboard
import time
import pyautogui

run = False


def start(interval, delay):

    # setup
    global run
    run = True

    pyautogui.PAUSE = 0.05

    time.sleep(int(delay))

    wait = float(interval) - 0.05

    # key check

    def keyPressed(key):

        global run

        if str(key) == 'Key.esc':
            run = False

    listener = keyboard.Listener(on_press=keyPressed)
    listener.start()

    # main loop
    while run:
        pyautogui.click()
        time.sleep(wait)
