from lowadi.Page import Page


class HorseList(Page):
    url = "https://www.lowadi.com/elevage/chevaux/?elevage=all-horses"
    selectors = {
        "css": {
            "horses": "a.horsename[href]"
        }
    }

    def get_ids(self):
        if self.site.cache.horses_ids:
            return self.site.cache.horses_ids

        horses_selector = HorseList.selectors['css']['horses']
        horses = self.site.get_all_el_by.css(horses_selector)
        ids = map(lambda link: link.get_attribute('href'), horses)
        ids = list(ids)

        self.site.cache.horses_ids = ids

        return ids