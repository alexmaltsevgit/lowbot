import time

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

import lowadi


class Mating(lowadi.Page, lowadi.HasID):
    url = "https://www.lowadi.com/elevage/chevaux/rechercherMale?jument={id}"
    selectors = {
        "id": {
            "race_select": "race",
            "do_reproduction_btn": "boutonDoReproduction"
        },
        "tag": {
            "form": "form"
        },
        "xpath": {
            "race_option": "//*[@id=\"race\"]/*/*[contains(text(), '{race}')]",
        },
        "css": {
            "first_horse_btn": "#table-0 > tbody > tr:first-child > td.action > a"
        }
    }

    def __init__(self, site, id_):
        lowadi.Page.__init__(self, site)
        lowadi.HasID.__init__(self, id_)

    def mate(self, race):
        race_select = self.site.find_element(
            By.ID,
            self.selectors['id']['race_select']
        )
        race_option = self.site.find_element(
            By.XPATH,
            self.selectors['xpath']['race_option'].format(race=race)
        )

        self.site.click_on(race_select)
        self.site.click_on(race_option)

        form: WebElement = self.site.find_element(By.TAG_NAME, self.selectors['tag']['form'])
        form.submit()

        time.sleep(1)

        first_horse_btn = self.site.find_element(By.CSS_SELECTOR, self.selectors['css']['first_horse_btn'])
        self.site.click_on(first_horse_btn)

        do_reproduction_btn = self.site.find_element(By.ID, self.selectors['id']['do_reproduction_btn'])
        self.site.click_on(do_reproduction_btn)
