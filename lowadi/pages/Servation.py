import lowadi


class Servation(lowadi.Page, lowadi.HasID):
    url = "https://www.lowadi.com/elevage/chevaux/rechercherMale?jument={id}"
    selectors = {}

    def __init__(self, site, id_):
        lowadi.Page.__init__(self, site)
        lowadi.HasID.__init__(self, id_)
