from typing import Dict

from abc import abstractmethod


class Page:
    def __init__(self, site, window_handler=None):
        self.site = site
        self.window_handler = window_handler

    @property
    @abstractmethod
    def url(self) -> str:
        pass

    @property
    @abstractmethod
    def selectors(self) -> Dict[str, Dict[str, str]]:
        return {}
