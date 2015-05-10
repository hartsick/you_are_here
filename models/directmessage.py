from twitteruser import TwitterUser
from twitterobject import TwitterObject

class DirectMessage(TwitterObject):
    '''
        Class for a received Direct Message from the Twitter API.
        Provides easy access to commonly used attributes.
    '''
    def __init__(self, data):
        super(DirectMessage, self).__init__(data)

        # remove root if exists
        if data.get('direct_message'):
            self.data = data['direct_message']

        self.id = self.data['id']
        self.text = self.data['text']
        self.mentions = self.data['entities']['user_mentions']

    def sender_not_self(self):
        '''Boolean, Returns true if sender of DM is not the app's Twitter bot'''
        sender = self.sender()

        return sender.is_not_bot()

    def sender(self):
        '''Returns a TwitterUser object for the DM's sender'''
        sender_hash = self.data['sender']
        sender = TwitterUser(sender_hash)

        return sender

    def recipient(self):
        '''Returns a TwitterUser object for the DM's receipient'''
        recipient_hash = self.data['recipient']
        recipient = TwitterUser(recipient_hash)

        return recipient
