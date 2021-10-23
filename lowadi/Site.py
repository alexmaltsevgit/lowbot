import utils.decorators
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
        self._get_horses_ids()

    def proceed_horses(self):
        for id in self.cache.horses_ids:
            horse = lowadi.Horse(self, id)
            self._open_page_in_new_tab(horse)
            self._sign_up_to_ksk(id) if horse.needs_ksk() else None
            self._close_page(horse)

    def _sign_up_to_ksk(self, id: str):
        ksk = lowadi.KSK(self, id)
        old_tab = self._open_page_in_new_tab(ksk)
        ksk.sign_up()
        self._close_page(ksk, old_tab)

    def _get_horses_ids(self):
        horse_list = lowadi.HorseList(self)
        self._open_page(horse_list)
        self.cache.horses_ids = horse_list.get_ids()

    def _open_page_in_new_tab(self, page: lowadi.Page, get_parameters=None):
        old_tab = self.current_window_handle
        self.open_new_tab()
        self._open_page(page, get_parameters)

        return old_tab

    @utils.decorators.sleep_after(1)
    def _open_page(self, page: lowadi.Page, get_parameters=None):
        if get_parameters is None:
            get_parameters = {}

        url = page.url.format(**get_parameters)
        self.get(url)

        page.window_handler = self.current_window_handle

    @utils.decorators.sleep_after(1)
    def _close_page(self, page: lowadi.Page, tab_to_switch_back = None):
        back = tab_to_switch_back or self.window_handles[0]
        self.switch_to.window(page.window_handler)
        self.close()
        self.switch_to.window(back)
