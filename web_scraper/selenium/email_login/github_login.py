#!/usr/bin/python3.8

import sys
import os
import time
from os.path import join, dirname
from dotenv import load_dotenv
sys.path.append('/home/pit/Documents/py_env/general_env/lib/python3.8/site-packages')
from selenium import webdriver


def github_login():
    dotenv_path = join(dirname(__file__), '.env')
    load_dotenv(dotenv_path)

    my_browser = webdriver.Firefox()
    # send the browser to a specif URL
    my_browser.get('https://github.com/login')
    time.sleep(1)
    my_browser.find_element_by_css_selector('#login_field').send_keys(os.environ.get('GITHUB_USERNAME'))
    my_browser.find_element_by_css_selector('#password').send_keys(os.environ.get('GITHUB_PWD'))
    my_browser.find_element_by_css_selector('.btn').click()


github_login()
