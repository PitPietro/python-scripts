import pyautogui as gui
import pyperclip


def type_cmd(msg_l):
    for char in msg_l:
        pyperclip.copy(char)
        gui.hotkey('ctrl', 'V', interval=0.01)
