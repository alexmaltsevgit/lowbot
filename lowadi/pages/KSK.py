from selenium.webdriver.common.by import By

import lowadi


class KSK(lowadi.Page):
    url = "https://www.lowadi.com/elevage/chevaux/centreInscription?id={id}"
    selectors = {
        "css": {
            "ksk_60_days_tab": "#table-0 > thead > tr > .caption-module[colspan=5] > .grid-table > .grid-row > "
                               "span.grid-cell:last-child > a",
            "ksk_60_days_btn": "#table-0 > tbody > tr:first-child > td:nth-child(11) > button"
        }
    }

    def sign_up(self):
        ksk_60_days_tab = KSK.selectors['css']['ksk_60_days_tab']
        ksk_60_days_tab = self.site.find_element(By.CSS_SELECTOR, ksk_60_days_tab)
        self.site.click_on(ksk_60_days_tab)

        ksk_60_days_btn = KSK.selectors['css']['ksk_60_days_btn']
        ksk_60_days_btn = self.site.find_element(By.CSS_SELECTOR, ksk_60_days_btn)
        self.site.click_on(ksk_60_days_btn)
