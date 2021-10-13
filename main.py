from dotenv import load_dotenv
from selenium import webdriver
from fake_useragent import UserAgent
from time import sleep
import os

from moves.get_horses_links import get_horses_links
from moves.go_to_horselist import go_to_horselist
from moves.login import login


def get_options(user_agent):
    options = webdriver.ChromeOptions()
    options.add_argument(f"user-agent={user_agent.chrome}")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--start-maximized")

    return options


if __name__ == '__main__':
    load_dotenv()

    user_agent = UserAgent()

    options = get_options(user_agent)

    browser = webdriver.Chrome(
        executable_path=r"C:\Users\Sergey\PycharmProjects\lowbot\chromedriver.exe",
        options=options
    )

    login(browser)
    sleep(2)
    go_to_horselist(browser)
    sleep(2)
    hrefs = get_horses_links(browser)
    sleep(1)
    print(hrefs)
