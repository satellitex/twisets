# -*- coding: utf-8 -*-


class Environment(object):
    def __init__(self, twiloader):
        self._env = dict()
        self._loader = twiloader

    def get(self, key):
        value = self._env.get(key, None)
        if value is None:
            raise KeyError(key)
        return value

    def set(self, key, value):
        self._env[key] = value

    @property
    def twiloader(self):
        return self._loader
