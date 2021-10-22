import lowadi


class Horse(lowadi.Page):
    url: str = "https://www.lowadi.com/elevage/chevaux/cheval?id={id}"
    selectors = {
        "id": {
            "owner": "#ownerBoite",
        },
        "link_part": {
            "ksk": "elevage/chevaux/centreInscription?id=",
        },
    }

    def proceed(self):
        pass

    def needs_ksk(self):
        ksk_link = Horse.selectors['link_part']['ksk']
        return bool(
            self.site.get_el_by.link_part(ksk_link)
        )

    def is_proceedable(self):
        owner_id = Horse.selectors['id']['owner']
        return not bool(
            self.site.get_el_by.id(owner_id)
        )
