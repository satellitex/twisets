from twisets import twloader

# 集合オブジェクト
class Sets():
    def __init__(self, inout=None, id=None):
        if inout == None or id == None:
            self._sets = set()
        else:
            self._sets = twloader.TwiLoader().load(inout, id)

    def set(self, value):
        self._sets = value

    def get(self):
        return self._sets