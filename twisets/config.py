# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod
import yaml

class Config(object, metaclass=ABCMeta):
    CONSUMER_KEY = "consumer_key"
    CONSUMER_SECRET = "consumer_secret_key"
    ACCESS_KEY = "access_key"
    ACCESS_SECRET = "access_secret_key"


class YamlConfig(Config):
    def __init__(self, path):
        f = open(path,'r+')
        data = yaml.load(f)
        for key, value in data.items():
            setattr(self, key.upper(), value)