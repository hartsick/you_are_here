from twitterobject import TwitterObject
from twitteruser import TwitterUser

class Status(TwitterObject):
    '''
        Class for a received Status from the Twitter API.
        Provides easy access to commonly used attributes.
    '''
    def __init__(self, data):
        super(Status, self).__init__(data)
        self.mentions = self.data['entities']['user_mentions']
        self.text = self.data['text']
        self.id = self.data['id']
        self.id_str = self.data['id_str']
        self.type = 'tweet'

        # if retweet, evaluate nested data
        if data.get('retweeted_status'):
            self.data = data['retweeted_status']
            self.type = 'retweet'

    def sender(self):
        sender_hash = self.data['user']
        sender = TwitterUser(sender_hash)

        return sender

    def sender_not_self(self):
        '''Boolean, Returns true if follower is not the Twitter bot'''
        sender = self.sender()

        return sender.is_not_bot()

    def reply_to_status(self):
        '''
            Returns the id if the Status is a response to another Status, otherwise returns None.
        '''
        return reply_to_user() and self.data['in_reply_to_status_id']

    def reply_to_user(self):
        '''
            Returns TwitterUser object if Status is a direct response to a user, otherwise returns None.
        '''
        if self.data['in_reply_to_user_id']:
            for user_hash in self.mentions:
                if user_hash['id'] == self.data['in_reply_to_user_id']:
                    user = TwitterUser(user_hash)

                    return user

    def is_reply_to_bot(self):
        ''' Boolean. Returns true if the Status is a reply to the Twitter bot'''
        user = self.reply_to_user()

        return user and user.is_bot()


    #############################
    # Bot-specific methods below
    #############################
