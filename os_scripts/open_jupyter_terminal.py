#!/usr/bin/python3.8


import sys

sys.path.append('/home/pit/Documents/py_env/general_env/lib/python3.8/site-packages')
import pyautogui as gui
import pyperclip


def type_cmd(msg_l):
    for char in msg_l:
        pyperclip.copy(char)
        gui.hotkey('ctrl', 'V', interval=0.01)


def open_notebook():
    command = 'cd && cd Documents/py_env ' \
              '&& source notes_env/bin/activate ' \
              '&& cd && cd Documents/python_projects/jupyter_notes' \
              '&& python -m notebook ' \
              '&& firefox http://localhost:8888/notebooks/test_notebook.ipynb'
    gui.hotkey('ctrl', 'shift', 'T')
    type_cmd(command)
    gui.press('enter')


open_notebook()
