from dotenv import load_dotenv
from selenium import webdriver
from fake_useragent import UserAgent
import time
import os

from moves.login import login


def get_options(user_agent):
    options = webdriver.ChromeOptions()
    options.add_argument(f"user-agent={user_agent.chrome}")
    options.add_argument("--disable-blink-features=AutomationControlled")

    return options


if __name__ == '__main__':
    load_dotenv()

    user_agent = UserAgent()

    options = get_options(user_agent)

    browser = webdriver.Chrome(
        executable_path=r"D:\Projects\lowbot\chromedriver.exe",
        options=options
    )

    login(browser)
