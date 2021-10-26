import re

from selenium.common.exceptions import ElementNotInteractableException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

import lowadi
from utils.decorators import pass_exception


class Horse(lowadi.Page, lowadi.HasID):
    class Cache:
        info_table: WebElement = None

    url = "https://www.lowadi.com/elevage/chevaux/cheval?id={id}"
    selectors = {
        "id": {
            "owner": "ownerBoite",
            "info_table": "characteristics-body-content",
            "open_feed_btn": "boutonNourrir",
            "hay_slider": "haySlider",
            "oats_slider": "oatsSlider",
            "feed_btn": "feed-button",
            "clean_btn": "boutonPanser",
            "sleep_btn": "boutonCoucher"
        },
        "css": {
            "ksk_link": "a[href*=\"centreInscription\"]",
            "mating_btn": "a[href*=\"rechercherMale?jument\"]",
            "mission_btn": "#mission-body-content .middle > a",
        }
    }
    info_table_selectors = {
        "css": {
            "age": "tr:first-child > td:last-child",
            "sex": "tr:nth-child(3) > td:first-child",
            "race": "a[href*=\"/dossiers/race?qName\"]"
        },
    }

    def __init__(self, site, id_):
        lowadi.Page.__init__(self, site)
        lowadi.HasID.__init__(self, id_)
        self.cache = Horse.Cache()

    def proceed(self):
        if not self._is_young():
            self._click_mission()
            self._feed()

        self._clean()
        self._sleep()

    def needs_ksk(self):
        ksk_link = self.selectors['css']['ksk_link']
        return bool(
            self.site.find_noexcept(By.CSS_SELECTOR, ksk_link)
        )

    def needs_mating(self):
        mating_btn_selector = self.selectors['css']['mating_btn']
        mating_btn = self.site.find_noexcept(By.CSS_SELECTOR, mating_btn_selector)

        return bool(mating_btn)

    def get_race(self):
        info_table = self.__get_info_table()

        race_selector = self.info_table_selectors['css']['race']
        race_link = info_table.find_element(By.CSS_SELECTOR, race_selector)
        race = race_link.text

        return race

    def _click_mission(self):
        mission_btn_selector = self.selectors['css']['mission_btn']
        mission_btn = self.site.find_element(By.CSS_SELECTOR, mission_btn_selector)
        self.site.click_on(mission_btn)

    def _feed(self):
        open_btn_selector = self.selectors['id']['open_feed_btn']
        open_btn = self.site.find_element(By.ID, open_btn_selector)
        self.site.click_on(open_btn)

        hay_slider_selector = self.selectors['id']['hay_slider']
        oats_slider_selector = self.selectors['id']['oats_slider']

        hay_slider: WebElement = self.site.find_element(By.ID, hay_slider_selector)
        oats_slider: WebElement = self.site.find_element(By.ID, oats_slider_selector)

        self.__click_last_active_li_in_slider(hay_slider)
        self.__click_last_active_li_in_slider(oats_slider)

        feed_btn_selector = self.selectors['id']['feed_btn']
        feed_btn = self.site.find_element(By.ID, feed_btn_selector)
        self.site.click_on(feed_btn)

    def _clean(self):
        clean_btn_selector = self.selectors['id']['clean_btn']
        clean_btn = self.site.find_element(By.ID, clean_btn_selector)
        self.site.click_on(clean_btn)

    def _sleep(self):
        sleep_btn_selector = self.selectors['id']['sleep_btn']
        sleep_btn = self.site.find_element(By.ID, sleep_btn_selector)
        self.site.click_on(sleep_btn)

    def is_proceedable(self):
        owner_id = self.selectors['id']['owner']
        return not bool(
            self.site.find_noexcept(By.ID, owner_id)
        )

    def _is_young(self):
        info_table = self.__get_info_table()

        age_selector = self.info_table_selectors['css']['age']
        age = info_table.find_element(By.CSS_SELECTOR, age_selector)
        age = age.text

        if 'лет' not in age:
            return True

        years = re.search(r'[0-9]+', age).group()
        return int(years) < 2

    def _is_female(self):
        info_table = self.__get_info_table()

        sex_selector = self.info_table_selectors['css']['sex']
        sex = info_table.find_element(By.CSS_SELECTOR, sex_selector)
        sex = sex.text.lower()

        return sex == 'кобыла'

    @pass_exception(ElementNotInteractableException)
    def __click_last_active_li_in_slider(self, slider: WebElement) -> WebElement:
        lasts_selector = "li:not(.disabled)"
        last = slider.find_elements(By.CSS_SELECTOR, lasts_selector)[-1]
        self.site.click_on(last)

    def __get_info_table(self) -> WebElement:
        info_table = self.cache.info_table
        try:
            info_table.is_enabled()
            return info_table
        except Exception:
            info_table: WebElement = self.site.find_element(
                By.ID,
                self.selectors['id']['info_table']
            )
            self.cache.info_table = info_table
            return info_table
