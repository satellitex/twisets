# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod


class TwiLoader(object, metaclass=ABCMeta):
    def __init__(self, *, twitter=None, db=None):
        if db == None:
            self._db = db
        self._db = dict()

    @abstractmethod
    def load(self, io, id):
        """

        :param io: ">" or "<", "<": follow, ">": follower.
        :param id: twitter_id
        :return: set of twitter_id's follow or follower.
        """
        pass