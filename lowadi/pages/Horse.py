from selenium.webdriver.common.by import By

import lowadi


class Horse(lowadi.Page, lowadi.HasID):
    url: str = "https://www.lowadi.com/elevage/chevaux/cheval?id={id}"
    selectors = {
        "id": {
            "owner": "ownerBoite",

        },
        "css": {
            "ksk_link": "a[href*=\"centreInscription\"]"
        }
    }

    def __init__(self, site, id):
        lowadi.Page.__init__(self, site)
        lowadi.HasID.__init__(self, id)

    def proceed(self):
        pass

    def needs_ksk(self):
        ksk_link = Horse.selectors['css']['ksk_link']
        return bool(
            self.site.find_element(By.CSS_SELECTOR, ksk_link)
        )

    def is_proceedable(self):
        owner_id = Horse.selectors['id']['owner']
        return not bool(
            self.site.find_element(By.ID, owner_id)
        )

    def is_young(self):
        pass
