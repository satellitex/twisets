from abc import ABCMeta, abstractmethod

class DB(object, metaclass=ABCMeta):

    @abstractmethod
    def __getitem__(self, item):
        """
        :param item: string
        :return set
        """
        pass

    @abstractmethod
    def __setitem__(self, key, value):
        """
        :param key: string
        :param value: set
        """
        pass


class OnMemoryDB(DB):
    def __init__(self):
        self._db = dict()

    def __getitem__(self, item):
        return self._db[item]

    def __setitem__(self, key, value):
        self._db[key] = value