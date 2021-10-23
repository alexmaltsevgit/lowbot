from typing import Dict

from abc import abstractmethod


class Page:
    def __init__(self, site):
        self.site = site
        self.window_handler = None

    @property
    @abstractmethod
    def url(self) -> str:
        pass

    @property
    @abstractmethod
    def selectors(self) -> Dict[str, Dict[str, str]]:
        return {}
