import os

from selenium import webdriver
from fake_useragent import UserAgent

from browser.WrappedChrome import WrappedChrome


def get_options(user_agent, is_headless=False):
    options = webdriver.ChromeOptions()
    options.add_argument(f"user-agent={user_agent.chrome}")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--start-maximized")

    if is_headless:
        options.add_argument("--headless")

    return options


def instantiate_driver(is_headless=False):
    user_agent = UserAgent()
    options = get_options(user_agent, is_headless)
    webdriver_path = os.getenv('WEBDRIVER_PATH')
    driver = WrappedChrome(
        executable_path=webdriver_path,
        options=options
    )

    return driver