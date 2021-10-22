from browser.WrappedChrome import WrappedChrome
import lowadi


class Site(WrappedChrome):
    def __init__(self, homepage: str, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.homepage = homepage
        self.cache = lowadi.Cache()
        self.cookies = lowadi.Cookies(self)

    def init(self):
        home = lowadi.Home(self)
        self._open_page(home)
        home.login()
        self.get_horses_ids()

    def get_horses_ids(self):
        horse_list = lowadi.HorseList(self)
        self._open_page(horse_list)
        self.cache.horses_ids = horse_list.get_ids()
        print(self.cache.horses_ids)

    def _open_page_in_new_tab(self, page: lowadi.Page, get_parameters=None):
        self.open_new_tab()
        self._open_page(page, get_parameters)

    def _open_page(self, page: lowadi.Page, get_parameters=None):
        if get_parameters is None:
            get_parameters = {}

        url = page.url.format(**get_parameters)
        self.get(url)

        page.window_handler = self.current_window_handle

    def _close_page(self, page: lowadi.Page):
        self.switch_to.window(page.window_handler)
        self.close()
