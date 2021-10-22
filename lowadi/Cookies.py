import os
import pickle
from pathlib import Path

from browser.WrappedChrome import WrappedChrome


class Cookies:
    filename_suffix = '_cookies'

    def __init__(self, driver: WrappedChrome):
        username = os.getenv('LOWADI_USERNAME')
        self.filename = username + Cookies.filename_suffix
        self.__driver = driver

    def load(self):
        for cookie in pickle.load(open(self.filename, 'rb')):
            self.__driver.add_cookie(cookie)

    def save(self):
        cookies = self.__driver.get_cookies()
        pickle.dump(cookies, open(self.filename, 'wb'))

    def exist(self):
        path = Path(self.filename)
        return path.is_file()
