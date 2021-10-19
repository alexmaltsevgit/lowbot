from os import getenv

from lowadi.selectors import selectors
from browser.WrappedChrome import WrappedChrome
from lowadi.Cache import Cache


class Site:
    def __init__(self, driver: WrappedChrome, username: str, password: str):
        self.__driver = driver
        self.__cache = Cache()
        self.__username = username
        self.__password = password

        self.__pages = {
            "home": getenv("LOWADI_HOME_PAGE"),
            "horses": getenv("LOWADI_HORSELIST_PAGE")
        }
        self.__page_selectors = {}

    def login(self):
        self.__open_page('home')

        self.__driver.click_on_many([
            self.__page_selectors['accept_cookie_btn'],
            self.__page_selectors['open_login_form_btn'],
        ])

        self.__driver.fill_many_fields({
            self.__page_selectors['username_field']: self.__username,
            self.__page_selectors['password_field']: self.__password
        })

        submit = self.__page_selectors['login_form_submit_btn']
        self.__driver.click_on(submit)

    def get_horses_links(self):
        if self.__cache.horses_links:
            return self.__cache.horses_links

        main_tab, horses_tab = self.__driver.open_new_tab()
        self.__open_page('horses')

        horses_selector = self.__page_selectors['horses']
        horses = self.__driver.find_all(horses_selector)
        hrefs = map(lambda link: link.get_attribute('href'), horses)
        hrefs = list(hrefs)

        self.__cache.horses_links = hrefs

        self.__driver.close()
        self.__driver.switch_to.window(main_tab)

        return hrefs

    def __open_page(self, page: str):
        url = self.__pages[page]
        self.__driver.get(url)
        self.__page_selectors = selectors[page]
