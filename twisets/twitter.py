import json
from requests_oauthlib import OAuth1Session  #OAuthのライブラリの読み込み
from abc import ABCMeta, abstractmethod

class TwitterClient(object, metaclass=ABCMeta):
    def __init__(self):
        pass

    @abstractmethod
    def get(self, io, id):
        """
        :param io: ">" or "<", "<": follow, ">": follower.
        :param id: twitter_id
        :return: set of twitter_id's follow or follower.
        """
        pass


class MockTwitterClient(TwitterClient):
    def __init__(self):
        super().__init__()

    def get(self, io, id):
        return {id}