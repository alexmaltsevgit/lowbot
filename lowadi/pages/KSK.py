from selenium.webdriver.common.by import By

import lowadi


class KSK(lowadi.Page, lowadi.HasID):
    url = "https://www.lowadi.com/elevage/chevaux/centreInscription?id={id}"
    selectors = {
        "xpath": {
            "ksk_60_days_tab": "/html/body/div[7]/main/section/section/div[1]/table/thead/tr/td[6]/span[2]/span/span["
                               "9]/a",
            "ksk_60_days_btn": "/html/body/div[7]/main/section/section/div[1]/table/tbody/tr[1]/td[10]/button"
        }
    }

    def __init__(self, site, id):
        lowadi.Page.__init__(self, site)
        lowadi.HasID.__init__(self, id)

    def sign_up(self):
        ksk_60_days_tab = KSK.selectors['xpath']['ksk_60_days_tab']
        ksk_60_days_tab = self.site.find_element(By.XPATH, ksk_60_days_tab)
        self.site.click_on(ksk_60_days_tab)

        ksk_60_days_btn = KSK.selectors['xpath']['ksk_60_days_btn']
        ksk_60_days_btn = self.site.find_element(By.XPATH, ksk_60_days_btn)
        self.site.click_on(ksk_60_days_btn)

        alert = self.site.switch_to.alert
        alert.accept()
