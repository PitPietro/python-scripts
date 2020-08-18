from datetime import datetime

from gtts import gTTS
from time import sleep
from selenium import webdriver
import pyautogui as p_gui


def open_file(path):
    with open(path, 'r') as my_file:
        text_lines = my_file.readlines()
        print(my_file)
    return text_lines


def open_firefox(username, password):
    my_browser = webdriver.Firefox()
    my_browser.get('https://accounts.google.com/signin/v2/identifier')

    usr_el = my_browser.find_element_by_css_selector('#identifierId')
    usr_el.send_keys(username)
    usr_el.submit()

    # login_1 = my_browser.find_element_by_css_selector('.VfPpkd-RLmnJb')
    # login_1.click()

    sleep(2)

    pdw_el = my_browser.find_element_by_css_selector('.I0VJ4d > div:nth-child(1) > input:nth-child(1)')
    pdw_el.send_keys(password)

    login_2 = my_browser.find_element_by_css_selector('.VfPpkd-LgbsSe-OWXEXe-k8QpJ > div:nth-child(3)')
    login_2.click()

    sleep(2)

    my_browser.get('https://mail.google.com/mail/u/0/#inbox')

    sleep(2)
    return my_browser


def read_single_mail(browser, prev_id, obj, body):
    prev_el = browser.find_element_by_id(prev_id)
    prev_el.click()
    sleep(2)

    obj_txt = browser.find_element_by_id(obj).text
    # sender_txt = browser.find_element_by_id(sender).text
    body_txt = browser.find_element_by_css_selector(body)
    msg = 'Object: {}. Content {}'.format(obj_txt, body_txt)
    return msg, obj_txt


def recon(image_path):
    img = p_gui.locateCenterOnScreen(image_path)
    p_gui.click(img)
    print(img)


def speech_1(text, sender):
    msg = 'Sender: {}. Object: {}'.format(sender, text)
    tts = gTTS(text=msg, lang='en')
    now = datetime.now()
    title = sender.replace(' ', '_') + now.strftime('_%d-%m-%y_%H-%M-%S') + '.mp3'
    print(title)
    tts.save(title)
    print('_________________________________________________________________')


def main():
    usr, pdw = open_file('credential.txt')
    b = open_firefox(usr, pdw)
    t, s = read_single_mail(b, ':1v', ':kf', '#\:l1 > div:nth-child(1)')
    speech_1(t, s)


if __name__ == '__main__':
    main()
