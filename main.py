import time

from dotenv import load_dotenv
from os import getenv

from lowadi.Site import Site
from instantiate_browser import instantiate_driver

if __name__ == '__main__':
    load_dotenv()

    username = getenv("LOWADI_USERNAME")
    password = getenv("LOWADI_PASSWORD")

    driver = instantiate_driver()
    lowadi = Site(
        driver,
        username,
        password
    )

    try:
        lowadi.login()
        lowadi.get_horses_links()
    except:
        driver.quit()
