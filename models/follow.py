from twitterobject import TwitterObject
from twitteruser import TwitterUser

class Follow(TwitterObject):
    '''
        Class for a received Follow from the Twitter API.
        Provides easy access to commonly used attributes.
    '''

    def recipient(self):
        '''Returns a TwitterUser object for the user being followed'''
        recipient_hash = self.data['target']
        recipient = TwitterUser(recipient_hash)

        return recipient

    def sender(self):
        '''Returns a TwitterUser object for the follower'''
        sender_hash = self.data['source']
        sender = TwitterUser(sender_hash)

        return sender

    def sender_not_self(self):
        '''Boolean, Returns true if follower is not the app's Twitter bot'''
        sender = self.sender()

        return sender.is_not_bot()
