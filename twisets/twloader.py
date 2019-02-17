class TwiLoader():
    def __init__(self, db=None):
        if db == None:
            self._db = db
        self._db = dict()

    def __call__(self, *args, **kwargs):
        pass

    def load(self, io, id):
        pass