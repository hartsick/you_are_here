import os

twitter_cred = [
    os.environ.get('MASTER_BOT_CONSUMER_KEY'),
    os.environ.get('MASTER_BOT_CONSUMER_SECRET'),
    os.environ.get('YOUAREHERE_ACCESS_TOKEN'),
    os.environ.get('YOUAREHERE_ACCESS_TOKEN_SECRET')
]

BOT_ID = 3190153903

tweet_locally = os.environ.get('TWEET_LOCAL', None)

# BOT-SPECIFIC CONFIG
follow_back = False
