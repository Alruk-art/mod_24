#!/usr/bin/python3
# -*- encoding=utf8 -*-

# You can find very simple example of the usage Selenium with PyTest in this file.
#
# More info about pytest-selenium:
#    https://pytest-selenium.readthedocs.io/en/latest/user_guide.html
#
# How to run:
#  1) Download geko driver for Chrome here:
#     https://chromedriver.storage.googleapis.com/index.html?path=2.43/
#  2) Install all requirements:
#     pip install -r requirements.txt
#  3) Run tests:
#     python -m pytest -v --driver Chrome --driver-path c://brodriver/chromedriver.exe  test_selenium_simple.py
#

import time


def test_search_example(selenium):
    """ Search some phrase in google and make a screenshot of the page. """

    # Open google search page:
    selenium.get('https://google.com')

    time.sleep(5)  # just for demo purposes, do NOT repeat it on real projects!

    # Find the field for search text input:
    search_input = selenium.find_element_by_name('q')

    # Enter the text for search:
    search_input.clear()
    search_input.send_keys('garmin 245')

    time.sleep(3)  # just for demo purposes, do NOT repeat it on real projects!

    # Click Search:
    search_button = selenium.find_element_by_name("btnK")
    search_button.click()


    time.sleep(3)  # just for demo purposes, do NOT repeat it on real projects!

    # Make the screenshot of browser window:
    selenium.save_screenshot('result.png')

    selenium.get ('https://pytest-selenium.readthedocs.io/en/latest/user_guide.html')
    xpath_conf_file = '(//body/div[1]/section/div/div/div[2]/div/div/div[1]/ul/li/ul/li[2]/a)'
    element = selenium.find_element_by_xpath (xpath_conf_file)
    #xpath = '//*[text()="configuration file"]'
    #elements = selenium.find_element_by_xpath (xpath)
    element.click()


