#!/usr/bin/python3.8

import sys
sys.path.append('/home/pit/Documents/py_env/general_env/lib/python3.8/site-packages')
from selenium import webdriver
import argparse


def start_website():
    my_browser = webdriver.Firefox()
    # send the browser to a specif URL
    my_browser.get('https://web.telegram.org/#/im')
    # nom_el = my_browser.find_element_by_css_selector('#trNominativoRitiro > td:nth-child(2) > input:nth-child(1)')


start_website()
