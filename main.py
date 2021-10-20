import time

from dotenv import load_dotenv
from os import getenv

from lowadi.Site import Site
from bootstrap.instantiation import *

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

    lowadi.login()
