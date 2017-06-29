import urllib.request, urllib.parse
import json
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
   print(channel_messages)
   call(['vlc', '-f https://www.youtube.com/watch?v=cTSjyXL4_MQ'])
   exit()
   for channel_message in channel_messages:
       if type == 'message' and len(channel_message['attachments']) and channel_message['attachments'][0] == 'YouTube':
            call(['vlc', '-f ' + channel_message['text'][1:-1]])
print('end')