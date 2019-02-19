from abc import ABCMeta, abstractmethod


class DB(object, metaclass=ABCMeta):
    def __getitem__(self, item):
        """
        :param item: string
        :return set
        """
        pass

    def __setitem__(self, key, value):
        """
        :param key: string
        :param value: set
        """
        pass
