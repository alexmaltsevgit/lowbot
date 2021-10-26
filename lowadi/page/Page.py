from typing import Dict

from abc import abstractmethod


class Page:
    class Meta:
        opened_by = None

    def __init__(self, site):
        self.site = site
        self.window_handler = None
        self.meta = Page.Meta()

    @property
    @abstractmethod
    def url(self) -> str:
        pass

    @property
    @abstractmethod
    def selectors(self) -> Dict[str, Dict[str, str]]:
        return {}

    def __enter__(self):
        old_tab = self.site.open_page_in_new_tab(self)
        self.meta.opened_by = old_tab

        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.site.close_page(self, self.meta.opened_by)
