import urllib.request
slack_endpoint = 'https://slack.com/api/'
uri = 'channels.history'
params = ''
full_url = ''
with urllib.request.urlopen(full_url) as response:
   json = response.read()
   print(json)
print('end')