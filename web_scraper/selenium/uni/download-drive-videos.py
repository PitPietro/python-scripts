#!/usr/bin/python3.8

import sys
import os
import time
from os.path import join, dirname
from dotenv import load_dotenv
sys.path.append('/home/pit/Documents/py_env/general_env/lib/python3.8/site-packages')
from selenium import webdriver


def login():
    dotenv_path = join(dirname(__file__), '.env')
    load_dotenv(dotenv_path)

    my_browser = webdriver.Firefox()
    # send the browser to a specif URL
    my_browser.get('https://accounts.google.com/signin/v2/identifier')
    # find the username label and send the username value to it
    my_browser.find_element_by_css_selector('#identifierId') \
        .send_keys(os.environ.get('EMAIL_USR'))
    # find the first submit button and click on it
    my_browser.find_element_by_css_selector('.VfPpkd-RLmnJb').click()

    # wait for the username to the checked
    time.sleep(2)

    # inside the uni login
    # find the username label
    my_browser.find_element_by_css_selector('#username') \
        .send_keys(os.environ.get('UNI_USR'))

    # find the password label and send the password value to it
    my_browser.find_element_by_css_selector('#password') \
        .send_keys(os.environ.get('EMAIL_PWD'))

    # find the first submit button and click on it
    my_browser.find_element_by_css_selector('button.form-element').click()

    # find the second submit button and click on it
    # my_browser.find_element_by_css_selector('.VfPpkd-LgbsSe-OWXEXe-k8QpJ > div:nth-child(3)').click()
    # redirect to the inbox
    time.sleep(2)
    my_browser.get('https://drive.google.com')


def main():
    login()


main()
