from typing import Callable

from browser.WrappedChrome import WrappedChrome


def parse_get_parameters(url: str) -> dict:
    parameters = url.split('?')[1]
    parameters = parameters.split('&')
    parameters = map(lambda parameter: parameter.split('='), parameters)
    parameters = list(parameters)
    parameters = {parameter[0]: parameter[1] for parameter in parameters}

    return parameters


def in_new_tab(driver: WrappedChrome, callback: Callable, url: str = ""):
    old_tab, new_tab = driver.open_new_tab(url)
    callback()
    driver.close()
    driver.switch_to.window(old_tab)
