class HasID:
    def __init__(self, id_):
        self.id_ = id_
        self.url = self.url.format(id=id_)
