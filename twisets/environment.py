# -*- coding: utf-8 -*-


class Environment(object):
    def __init__(self, parent_env, twiloader=None):
        self._parent_env = parent_env
        self._env = dict()
        if twiloader == None:
            self._loader = parent_env.twiloader
        else:
            self._loader = twiloader

    def get(self, key):
        value = self._env.get(key, None)
        if not value:
            value = self._parent_env.get(key)
        return value

    def set(self, key, value):
        self._env[key] = value

    @property
    def twiloader(self):
        return self._loader
