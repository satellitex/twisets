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
        super(MockTwitterClient, self).__init__()

    def get(self, io, id):
        return {id}


class TwitterAPIClient(TwitterClient):
    def __init__(self, conf):
        super(TwitterAPIClient, self).__init__()
        consumer_key = conf.CONSUMER_KEY
        consumer_secret = conf.CONSUMER_SECRET
        access_token = conf.ACCESS_KEY
        access_secret = conf.ACCESS_SECRET

        # 認証
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_secret)

        self.api = tweepy.API(auth, wait_on_rate_limit=True)

    def get(self, io, id):
        ret_ids = []
        if io == ">":
            for followers in tweepy.Cursor(self.api.followers_ids,
                                     screen_name = id, stringify_ids=True, count=5000).pages():
                ret_ids.extend(followers)

        elif io == "<":
            for friends in tweepy.Cursor(self.api.friends_ids,
                                           screen_name=id, stringify_ids=True, count=5000).pages():
                ret_ids.extend(friends)
        else:
            raise NotImplementedError("io code is ",io)
        return set(ret_ids)