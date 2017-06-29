import urllib.request, urllib.parse
from config import config

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
   json = response.read()
   print(json)
print('end')