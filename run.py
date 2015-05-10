import logging
from time import sleep
from multiprocessing import Process
from twitter.userstream import UserStreamer
from config.common import twitter_cred

def run_user_stream():
    # start Twitter stream for user, restart with delay on crash
    #   -- for detecting user interaction with bot
    while True:
        try:
            print "Starting stream..."
            stream = UserStreamer(*twitter_cred)
            print stream.user(**{'with': 'user'})
        except Exception as e:
            logging.exception(e)
            sleep(60)

        sleep(60)

if __name__ == "__main__":

    run_user_stream()

    # p1 = Process(target=run_user_stream)

    # # TODO: add periodic random tweets
    # processes = [
    #     p1
    # ]

    # for process in processes:
    #     process.start()

    # for process in processes:
    #     process.join()
