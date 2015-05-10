from basestream import StreamListener
from rest import Tweeta
from config.common import follow_back

class UserStreamer(StreamListener):
    '''
        Defines event handlers for the User stream
    '''

    def on_direct_message(self, dm):
        pass

    def on_follow(self, follow):
        if follow_back:
            Tweeta().follow_back(follow)

    def on_reply(self, status):
        if status.sender_not_self() and status.is_reply_to_bot():
            # respond appropriately
            Tweeta().reply_to_status(status)
