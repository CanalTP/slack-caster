import urllib.request, urllib.parse
import json
from message import getLastMessageTs, setLastMessageTs
from config import config 
from subprocess import call

slack_endpoint = 'https://slack.com/api/'
uri = 'channels.history'
params = urllib.parse.urlencode({
    "token": config['slack-token'],
    "channel": config['channel-id-to-pull']
})
full_url = '?'.join([slack_endpoint + uri, params])
print(full_url)
# https://slack.com/api/channels.history?token=xoxp-16812062839-41309578433-204906609120-73921600c18cbcaa82217e35004a59ff&channel=C60NEG4QG&pretty=1
with urllib.request.urlopen(full_url) as response:
    channel_messages = json.loads(response.read().decode())
    print(len(channel_messages))
    # call(['vlc', '-f', 'https://www.youtube.com/watch?v=cTSjyXL4_MQ'])
    for channel_message in channel_messages['messages']:
        if channel_message['type'] == 'message' and 'attachments' in channel_message and len(
                channel_message['attachments']) > 0 and channel_message['attachments'][0]['service_name'] == 'YouTube':
            print(channel_message['attachments'][0]['from_url'])
            print(channel_message['ts']) 
            url_to_read = channel_message['attachments'][0]['from_url']
            if channel_message['ts'] > getLastMessageTs():
            	call(['vlc', '-f', url_to_read])
            	setLastMessageTs(channel_message['ts']);
print('end')
