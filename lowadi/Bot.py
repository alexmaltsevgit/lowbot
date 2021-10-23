import lowadi


class Bot(lowadi.Site):
    def init(self):
        home = lowadi.Home(self)
        self.open_page(home)
        home.login()
        self._get_horses_ids()

    def proceed_horses(self):
        for id in self.cache.horses_ids:
            with lowadi.Horse(self, id) as horse:
                self._sign_up_to_ksk(id) and self.refresh() if horse.needs_ksk() else None

    def _sign_up_to_ksk(self, id: str):
        with lowadi.KSK(self, id) as ksk:
            ksk.sign_up()

    def _get_horses_ids(self):
        horse_list = lowadi.HorseList(self)
        self.open_page(horse_list)
        self.cache.horses_ids = horse_list.get_ids()
