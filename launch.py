import urllib.request, urllib.parse
import json
from message import getLastMessageTs, setLastMessageTs
from config import config
from subprocess import call
import os
import time

slack_endpoint = 'https://slack.com/api/'
uri = 'channels.history'
params = urllib.parse.urlencode({
    "token": config['slack-token'],
    "channel": config['channel-id-to-pull']
})
full_url = '?'.join([slack_endpoint + uri, params])
# https://slack.com/api/channels.history?token=xoxp-16812062839-41309578433-204906609120-73921600c18cbcaa82217e35004a59ff&channel=C60NEG4QG&pretty=1
while True:
    print('pull from url ' + full_url)
    with urllib.request.urlopen(full_url) as response:
        channel_messages = json.loads(response.read().decode())
        print(len(channel_messages))
        # call(['vlc', '-f', 'https://www.youtube.com/watch?v=cTSjyXL4_MQ'])
        for channel_message in channel_messages['messages']:
            if channel_message['type'] == 'message' and 'attachments' in channel_message and len(
                    channel_message['attachments']) > 0 and channel_message['attachments'][0]['service_name'] == 'YouTube':
                url_to_read = channel_message['attachments'][0]['from_url']
                print(url_to_read)
                executable = config['video-player']
                if str(os.sep) in executable:
                    exec_parts = executable.split(os.sep)
                    executable_dir = os.sep.join(exec_parts[:-1])
                    print("chdir to " + executable_dir)
                    os.chdir(executable_dir)
                    executable = exec_parts[-1:]
                print(executable)
                # call(["vlc.exe", "-f", "https://www.youtube.com/watch?v=s5-nUCSXKac"])
                if channel_message['ts'] > getLastMessageTs():
                    call([executable, '--play-and-exit', '-f', url_to_read])
                    setLastMessageTs(channel_message['ts'])
    print('waiting 5s')
    time.sleep(5)
