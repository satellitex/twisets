# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod
import tweepy

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


class TwitterAPIClient(TwitterClient):
    def __init__(self, conf):
        consumer_key = conf.COSUMER_KEY
        consumer_secret = conf.CONSUMER_SECRET
        access_token = conf.ACCESS_KEY
        access_secret = conf.ACCESS_SECRET

        # 認証
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_secret)

        self.api = tweepy.API(auth, wait_on_rate_limit=True)

    def get(self, io, id):
        pass