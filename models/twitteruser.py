from config.common import BOT_ID

class TwitterUser(object):
    '''
        Given a User hash without root from the Twitter API, returns
        a User object with easy access to frequently-used attributes
    '''
    def __init__(self, data):
        self.data = data

        self.username = self.data['screen_name']
        self.display_name = self.data['name']
        self.id = self.data['id']

    def is_not_bot(self):
        '''Boolean, returns true if user is not the app's Twitter bot'''
        return not self.is_bot()

    def is_bot(self):
        '''Boolean, returns true if user is the app's Twitter bot'''
        return self.id == BOT_ID
