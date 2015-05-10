from twython import TwythonStreamer
from models.directmessage import DirectMessage
from models.follow import Follow
from models.status import Status

class StreamListener(TwythonStreamer):
    '''
        As event is received from stream, instantiates a new object of that type and calls the appropriate handler. Handlers must be implemented by subclass. Similar to Tweepy's StreamListener.
    '''

    def on_success(self, data):
        event_type = "untracked"

        if data.get('direct_message'):
            event_type = "Direct Message"

            dm = DirectMessage(data)
            self.on_direct_message(dm)

        elif data.get('event') and data['event'] == 'follow':
            event_type = "Follow"

            follow = Follow(data)
            self.on_follow(follow)

        elif data.get('text'):
            event_type = "Status"
            status = Status(data)

            # ignore RTs for now
            if status.type is 'retweet':
                event_type = "{0} -- Retweet".format(event_type)
            else:
                # if it's a reply, handle as such
                # otherwise, for now, do nothing.
                if status.reply_to_user():
                    event_type = "{0} -- Reply".format(event_type)
                    self.on_reply(status)

        print "{0} data received. Type: {1}".format(self.__class__.__name__, event_type)
        print data

    def on_error(self, status_code, data):
        print "{0} error: {1} | {2}".format(self.__class__.__name__, status_code, data)
