# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod


class TwiLoader(object):
    def __init__(self, *, twitter=None, db=None, use_cache=True):
        if db == None:
            self._db = dict()
        self._db = db
        self._twitter = twitter
        self._use_cache = use_cache

    def load(self, io, id):
        sid = io + id
        if (not self._use_cache) or (not sid in self._db):
            self._db[sid] = self._twitter.get(io, id)
        return self._db[sid]

    def screen_names(self, ids):
        return self._twitter.screen_names(ids)