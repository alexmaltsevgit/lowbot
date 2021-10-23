from selenium.webdriver.common.by import By

import utils.helpers
from lowadi.Page import Page


class HorseList(Page):
    url = "https://www.lowadi.com/elevage/chevaux/?elevage=all-horses"
    selectors = {
        "id": {
            "filter_dropdown": "horseFilterFiltre"
        },
        "css": {
            "horses": "a.horsename[href]",
            "noksk_filter_option": "#horseFilter > option[value=\"nocenter\"]"
        }
    }

    def get_ids(self):
        if self.site.cache.horses_ids:
            return self.site.cache.horses_ids

        horses_selector = HorseList.selectors['css']['horses']
        horses = self.site.find_elements(By.CSS_SELECTOR, horses_selector)
        hrefs = map(lambda link: link.get_attribute('href'), horses)
        ids = list(map(
            lambda get_parameters: utils.helpers.parse_get_parameters(get_parameters)['id'],
            hrefs
        ))

        self.site.cache.horses_ids = ids

        return ids
