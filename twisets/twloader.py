# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod


class TwiLoader(object):
    def __init__(self, *, twitter=None, db=None):
        if db == None:
            self._db = db
        self._db = dict()
        self._twitter = twitter

    def load(self, io, id):
        sid = io + id
        if not sid in self._db:
            self._db[sid] = self._twitter.get(io, id)
        return self._db[sid]
