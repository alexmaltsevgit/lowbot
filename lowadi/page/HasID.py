class HasID:
    def __init__(self, id):
        self.id = id
        self.url = self.url.format(id=id)
