import undetected_chromedriver.v2 as uc

import lowadi


def get_options(is_headless=False):
    options = uc.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument('--disable-popup-blocking')

    if is_headless:
        options.add_argument("--headless")

    return options


def instantiate_site(is_headless=False):
    options = get_options(is_headless)
    driver = lowadi.Bot(
        homepage="https://www.lowadi.com/",
        options=options
    )

    return driver
