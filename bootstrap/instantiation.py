import os

from selenium import webdriver
from fake_useragent import UserAgent

from lowadi.Site import Site


def get_options(is_headless=False):
    user_agent = UserAgent()
    options = webdriver.ChromeOptions()
    options.add_argument(f"user-agent={user_agent.chrome}")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--start-maximized")

    if is_headless:
        options.add_argument("--headless")

    return options


def instantiate_site(is_headless=False):
    options = get_options(is_headless)
    driver_path = os.getenv('WEBDRIVER_PATH')
    driver = Site(
        homepage="https://www.lowadi.com/",
        executable_path=driver_path,
        options=options
    )

    return driver
