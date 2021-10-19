import time
import os

from utils.sleep_after import sleep_after


def login(browser):
    browser.get("https://www.lowadi.com/")

    accept_cookie_btn = browser.find_element_by_css_selector('.grid-cell.even.last.pr--1')
    accept_cookie_btn.click()

    time.sleep(1)

    open_login_form_btn = browser.find_element_by_id('header-login-label')
    open_login_form_btn.click()

    time.sleep(1)

    username_field = browser.find_element_by_id('login')
    username_field.clear()
    username_field.send_keys(os.getenv('LOWADI_USERNAME'))

    time.sleep(1)

    password_field = browser.find_element_by_id('password')
    password_field.clear()
    password_field.send_keys(os.getenv('LOWADI_PASSWORD'))

    time.sleep(1)

    submit = browser.find_element_by_id('authentificationSubmit')
    submit.click()
