import undetected_chromedriver.v2 as uc

from lowadi.Site import Site


def get_options(is_headless=False):
    options = uc.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument('--disable-popup-blocking')

    if is_headless:
        options.add_argument("--headless")

    return options


def instantiate_site(is_headless=False):
    options = get_options(is_headless)
    driver = Site(
        homepage="https://www.lowadi.com/",
        options=options
    )

    return driver
