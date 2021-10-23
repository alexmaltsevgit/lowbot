import utils.decorators
from browser.WrappedChrome import WrappedChrome
import lowadi


class Site(WrappedChrome):
    def __init__(self, homepage: str, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.homepage = homepage
        self.cache = lowadi.Cache()
        self.cookies = lowadi.Cookies(self)

    def open_page_in_new_tab(self, page: lowadi.Page, get_parameters=None):
        old_tab = self.current_window_handle
        self.open_new_tab()
        self.open_page(page, get_parameters)

        return old_tab

    @utils.decorators.sleep_after(1)
    def open_page(self, page: lowadi.Page, get_parameters=None):
        if get_parameters is None:
            get_parameters = {}

        url = page.url.format(**get_parameters)
        self.get(url)

        page.window_handler = self.current_window_handle

    @utils.decorators.sleep_after(1)
    def close_page(self, page: lowadi.Page, tab_to_switch_back = None):
        back = tab_to_switch_back or self.window_handles[0]
        self.switch_to.window(page.window_handler)
        self.close()
        self.switch_to.window(back)
