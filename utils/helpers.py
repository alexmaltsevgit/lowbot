from typing import Callable

from browser.WrappedChrome import WrappedChrome


def in_new_tab(driver: WrappedChrome, callback: Callable, url: str = ""):
    old_tab, new_tab = driver.open_new_tab(url)
    callback()
    driver.close()
    driver.switch_to.window(old_tab)
