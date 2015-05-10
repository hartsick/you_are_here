import random
from twython import Twython
from config.common import twitter_cred, tweet_locally

class Tweeta(object):
    def __init__(self):
        self.twitter = Twython(*twitter_cred)

    def update_status(self, text):
        params = {'status': text}

        if tweet_locally:
            print "DEV: Updated status with: '{0}'".format(text)
        else:
            self.twitter.update_status(**params)

    def send_dm(self, text, user):
        params = {'text': text, 'user_id': user.id, 'screen_name': user.username}

        if tweet_locally:
            print "DEV: Sent DM: @{0} ({1}): '{2}'".format(user.username, user.id, text)
        else:
            self.twitter.send_direct_message(**params)

    def follow_back(self, follow):
        if follow.sender_not_self():
            user = follow.sender()
            params = {'user_id': user.id, 'screen_name': user.username}

            if tweet_locally:
                print "DEV: Friended {0} ({1})".format(user.username, user.id)
            else:
                self.twitter.create_friendship(**params)

    def retweet(self, status):
        params = {'id': status.id_str}

        if tweet_locally:
            print "DEV: Retweeted {0}".format(status.id_str)
        else:
            self.twitter.retweet(**params)

    def reply_to_status(self, status):
        print "reply received"
        if status.sender_not_self():
            # TODO: FORMAT TWEET
            text = ""

            response = "@{0} {1}".format(status.sender().username, text)

            params = {'status': response, 'in_reply_to_status_id': status.id}

            if tweet_locally:
                print "Responded with: {0}".format(response)
            else:
                self.twitter.update_status(**params)
