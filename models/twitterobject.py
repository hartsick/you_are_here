class TwitterObject(object):
    '''
        Abstract class / API Defnition for events received via Twitter API
        Most methods should be redefined by children
    '''
    def __init__(self, data):
        self.data = data
        self.text = None
