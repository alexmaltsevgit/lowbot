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
        # self._get_horses_ids()
        self.cache.horses_ids = ['70211944', '70192313', '70071350', '70071352', '69932418', '69790720', '69831095']

    def proceed_horses(self):
        for id in self.cache.horses_ids:
            horse = lowadi.Horse(self)
            self._open_page_in_new_tab(horse, {'id': id})
            self._sign_up_to_ksk(id) if horse.needs_ksk() else None
            self._close_page(horse)

    def _sign_up_to_ksk(self, id: str):
        ksk = lowadi.KSK(self)
        self._open_page_in_new_tab(ksk, {'id': id})
        ksk.sign_up()
        self._close_page(ksk)

    def _get_horses_ids(self):
        horse_list = lowadi.HorseList(self)
        self._open_page(horse_list)
        self.cache.horses_ids = horse_list.get_ids()

    def _open_page_in_new_tab(self, page: lowadi.Page, get_parameters=None):
        self.open_new_tab()
        self._open_page(page, get_parameters)

    @utils.decorators.sleep_after(1)
    def _open_page(self, page: lowadi.Page, get_parameters=None):
        if get_parameters is None:
            get_parameters = {}

        url = page.url.format(**get_parameters)
        self.get(url)

        page.window_handler = self.current_window_handle

    @utils.decorators.sleep_after(1)
    def _close_page(self, page: lowadi.Page, page_to_switch_back: lowadi.Page = None):
        back = page_to_switch_back.window_handler if page_to_switch_back else self.window_handles[0]
        self.switch_to.window(page.window_handler)
        self.close()
        self.switch_to.window(back)
