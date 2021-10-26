import lowadi
from utils.decorators import pass_exception


class Bot(lowadi.Site):
    def init(self):
        home = lowadi.Home(self)
        self.open_page(home)
        home.login()
        self._set_horses_ids()

    def proceed_horses(self):
        for id_ in self.cache.horses_ids:
            self._proceed_one_horse(id_)

    @pass_exception()
    def _proceed_one_horse(self, id_):
        with lowadi.Horse(self, id_) as horse:
            self._proceed_secondary(horse)
            horse.proceed()

    def _proceed_secondary(self, horse: lowadi.Horse):
        self._sign_up_to_ksk(horse.id_) if horse.needs_ksk() else None
        self._mate(horse.id_, horse.get_race()) if horse.needs_mating() else None
        self.refresh()

    def _sign_up_to_ksk(self, id_: str):
        with lowadi.KSK(self, id_) as ksk:
            ksk.sign_up()

    def _mate(self, id_: str, race: str):
        with lowadi.Mating(self, id_) as mating:
            mating.mate(race)

    def _set_horses_ids(self):
        horse_list = lowadi.HorseList(self)
        self.open_page(horse_list)
        self.cache.horses_ids = horse_list.get_ids()
