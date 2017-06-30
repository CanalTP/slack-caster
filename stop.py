import urllib.request, urllib.parse, urllib.error
import json
from message import getLastMessageTs, setLastMessageTs
from config import config
from constants import slack_endpoint, uri
import signal
import subprocess
import os
import time

last_message_ts = getLastMessageTs('_stop')
params = {
        "token": config['slack-token'],
        "count": 5,
        "channel": config['channel-id-to-pull']
    }
# https://slack.com/api/channels.history?token=xoxp-16812062839-41309578433-204906609120-73921600c18cbcaa82217e35004a59ff&channel=C60NEG4QG&pretty=1
while True:
    params["oldest"] = last_message_ts
    params_encoded = urllib.parse.urlencode(params)
    full_url = '?'.join([slack_endpoint + uri, params_encoded])
    print('pull from url ' + full_url)
    try:
        with urllib.request.urlopen(full_url) as response:
            channel_messages = json.loads(response.read().decode())
            print(len(channel_messages['messages']))
            # call(['vlc', '-f', 'https://www.youtube.com/watch?v=cTSjyXL4_MQ'])
            for channel_message in channel_messages['messages']:
                print(channel_message['ts'])
                print(channel_message['text'])
                if channel_message['type'] == 'message' and channel_message['text'] == 'stop' and channel_message['ts'] > getLastMessageTs():
                    print(config['platform'])
                    if config['platform'] == 'linux':
                        p = subprocess.Popen(['ps', '-A'], stdout=subprocess.PIPE)
                        out, err = p.communicate()
                        print(out)
                        exit()
                        for line in out.splitlines():
                            print(line)
                            if 'vlc' in line:
                                print('process vlc found ! waiting 3 seconds before kill !!!')
                                time.sleep(3)
                                pid = int(line.split(None, 1)[0])
                                os.kill(pid, signal.SIGKILL)
                    elif config['platform'] == 'windows':
                        os.system("taskkill /im vlc.exe")
                setLastMessageTs(channel_message['ts'], '_stop')
                last_message_ts = channel_message['ts']
        print('waiting 5s')
    except urllib.error.URLError:
        pass
    time.sleep(5)
