import lowadi


class Servation(lowadi.Page, lowadi.HasID):
    url = "https://www.lowadi.com/elevage/chevaux/rechercherMale?jument={id}"
    selectors = {}
