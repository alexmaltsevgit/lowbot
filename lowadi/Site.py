import pickle
import json
from os import getenv
from pathlib import Path
from time import sleep

from browser.WrappedChrome import WrappedChrome
from lowadi.Cache import Cache
from lowadi.Horse import Horse
from utils.decorators import sleep_after
from utils.helpers import in_new_tab


class Site:
    def __init__(self, driver: WrappedChrome, username: str, password: str):
        self.__driver = driver
        self.__cache = Cache()
        self.__username = username
        self.__password = password

        self.__cookies_filename = username + '_cookies'

        self.__pages = self.__read_pages_info()
        self.__selectors = ""

    def login(self):
        self.__open_page('home')
        if self.__cookies_exist():
            self.__login_by_cookies()
        else:
            self.__login_manually()

    def proceed_horses(self):
        links = self.__get_horses_links()
        for link in links:
            horse = Horse(
                self.__driver,
                link,
                self.__selectors
            )
            horse.proceed()
            sleep(1)

    def __login_by_cookies(self):
        in_new_tab(
            self.__driver,
            lambda: self.__load_cookies(),
            url=self.__pages['home']['url']
        )
        self.__driver.refresh()

    def __login_manually(self):
        self.__driver.click_on_many([
            self.__selectors['accept_cookie_btn'],
            self.__selectors['open_login_form_btn'],
        ])

        self.__driver.fill_many_fields({
            self.__selectors['username_field']: self.__username,
            self.__selectors['password_field']: self.__password
        })

        submit = self.__selectors['login_form_submit_btn']
        self.__driver.click_on(submit)

        self.__save_cookies()

    def __get_horses_links(self):
        if self.__cache.horses_links:
            return self.__cache.horses_links

        main_tab, horses_tab = self.__driver.open_new_tab()
        self.__open_page('all_horses')

        horses_selector = self.__selectors['horses']
        horses = self.__driver.find_all(horses_selector)
        hrefs = map(lambda link: link.get_attribute('href'), horses)
        hrefs = list(hrefs)

        self.__cache.horses_links = hrefs

        self.__driver.close()
        self.__driver.switch_to.window(main_tab)

        return hrefs

    def __load_cookies(self):
        for cookie in pickle.load(open(self.__cookies_filename, 'rb')):
            self.__driver.add_cookie(cookie)

    def __save_cookies(self):
        cookies = self.__driver.get_cookies()
        pickle.dump(cookies, open(self.__cookies_filename, 'wb'))

    def __cookies_exist(self):
        path = Path(self.__cookies_filename)
        return path.is_file()

    def __open_page(self, page: str):
        url = self.__pages[page]['url']
        selectors = self.__pages[page]['selectors']
        self.__selectors = selectors
        self.__driver.get(url)

    @staticmethod
    def __read_pages_info():
        with open("pages.json") as file:
            pages = json.load(file)
        return pages
