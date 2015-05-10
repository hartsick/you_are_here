import random
from time import sleep
from twython import Twython
from config.common import twitter_cred, tweet_locally
from gen_tweet import gen_response, get_street_view

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
        if status.sender_not_self():
            params = { 'in_reply_to_status_id': status.id }

            if status.location():
                img_path = get_street_view(status)
                img_id = self.upload_media(img_path)

                params['media_ids'] = [img_id]

            params['status'] = "@{0} {1}".format(status.sender().username, gen_response(status))

            print tweet_locally
            if tweet_locally is True:
                print "DEV: Responded with: {0}".format(params)
            else:
                print params
                self.twitter.update_status(**params)

    def upload_media(self, img_path):
        with open(img_path, 'r') as image_file:
            print("Uploading Image: %s" % img_path)

            upload_response = self.twitter.upload_media(media=image_file)
            print("Uploaded as media ID %s." % upload_response)

            media_id = upload_response['media_id']

            sleep(5)

        return media_id
