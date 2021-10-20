from selenium.common.exceptions import InvalidSelectorException

from browser.WrappedChrome import WrappedChrome


class Horse:
    def __init__(self, driver: WrappedChrome, url: str, selectors: dict[str]):
        self.__driver = driver
        self.__url = url
        self.__selectors = selectors

    def proceed(self):
        old_tab, new_tab = self.__driver.open_new_tab()
        self.__driver.get(self.__url)

        if self.__is_proceedable():
            self.__main()

        self.__driver.close()
        self.__driver.switch_to.window(old_tab)

    def __main(self):
        pass

    def __is_proceedable(self):
        try:
            owner_selector = self.__selectors['owner']
            _ = self.__driver.find(owner_selector)
            return False
        except InvalidSelectorException:
            return True
