import argparse
from time import sleep

from actions import SlackListener
from config import config

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument("-a", "--action", help="action", required=True)
    args = parser.parse_args()
    slack_endpoint = 'https://slack.com/api/'
    uri = 'channels.history'
    print(config)
    
    listener = SlackListener(slack_endpoint, uri, config, args.action)
    print(listener.last_message_ts)
    while True:
        listener.pull()
        sleep(5)
