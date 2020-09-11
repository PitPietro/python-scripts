#!/usr/bin/python3.8


import sys

sys.path.append('/home/pit/Documents/py_env/general_env/lib/python3.8/site-packages')
import pyautogui as gui
import pyperclip
import time


def type_cmd(msg_l):
    for char in msg_l:
        pyperclip.copy(char)
        gui.hotkey('ctrl', 'V', interval=0.01)


def open_notebook():
    cmd_1 = 'cd && cd Documents/py_env ' \
            '&& source notes_env/bin/activate ' \
            '&& cd && cd Documents/python_projects/jupyter_notes'
    cmd_2 = cmd_1 + ' && python -m notebook ' \
                    '&& firefox http://localhost:8888/'
    gui.hotkey('ctrl', 'shift', 'T')
    type_cmd(cmd_1)
    gui.press('enter')
    gui.hotkey('ctrl', 'shift', 'T')
    time.sleep(0.1)
    type_cmd(cmd_2)
    gui.press('enter')


open_notebook()
