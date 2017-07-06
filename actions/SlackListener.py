import json
from urllib import parse, request, error
from actions.Analyzer import Analyzer
from actions.matchers.StopMatcher import StopMatcher
from actions.matchers.YoutubeMatcher import YoutubeMatcher
from actions.executors.LinuxVlcExecutor import LinuxVlcExecutor
from actions.executors.LinuxVlcKiller import LinuxVlcKiller
from actions.executors.WindowsVlcExecutor import WindowsVlcExecutor
from actions.executors.WindowsVlcKiller import WindowsVlcKiller


class SlackListener:
    def __init__(self, slack_endpoint, uri, config, action):
        self.slack_endpoint = slack_endpoint
        self.uri = uri
        self.params = {
            "token": config['slack-token'],
            "count": 10,
            "channel": config['channel-id-to-pull']
        }
        self.action = action
        self.config = config
        self.init_from_platform(self.config['platform'], action)
        if self.timestamp_file_exists():
            self._last_message_ts = self.get_last_message_ts_from_file()
        else:
            self._last_message_ts = None

    def init_from_platform(self, platform, action):
        if action == 'launch':
            self.analyzers = [
                Analyzer(matcher=YoutubeMatcher(),
                         executor=eval(self.get_executor_from_platform(platform, 'vlc'))(self.config))
            ]
        elif action == 'control':
            self.analyzers = [
                Analyzer(matcher=StopMatcher(),
                         executor=eval(self.get_killer_from_platform(platform, 'vlc'))(self.config))
            ]

    def get_killer_from_platform(self, platform, application):
        return platform.title() + application.title() + 'Killer'

    def get_executor_from_platform(self, platform, application):
        return platform.title() + application.title() + 'Executor'

    @property
    def last_message_ts(self):
        return self._last_message_ts

    def get_timestamp_filename(self):
        return 'last_message_ts_' + self.action

    def get_last_message_ts_from_file(self):
        with open(self.get_timestamp_filename(), "r") as file:
            return file.readline()

    @last_message_ts.getter
    def last_message_ts(self):
        return self._last_message_ts

    @last_message_ts.setter
    def last_message_ts(self, value):
        print('last_message_ts.setter ' + value)
        with open(self.get_timestamp_filename(), "w") as file:
            file.write(value)
        self._last_message_ts = value

    def timestamp_file_exists(self):
        try:
            open(self.get_timestamp_filename(), "r")
            return True
        except FileNotFoundError:
            return False

    def pull(self):
        if self._last_message_ts:
            self.params['oldest'] = self._last_message_ts
        params_encoded = parse.urlencode(self.params)
        full_url = '?'.join([self.slack_endpoint + self.uri, params_encoded])
        print('pull from url ' + full_url)
        try:
            with request.urlopen(full_url) as response:
                channel_messages = json.loads(response.read().decode())
                if not 'messages' in channel_messages:
                    raise Exception(channel_messages)
                print(len(channel_messages['messages']))
                for channel_message in channel_messages['messages'][::-1]:
                    print(channel_message)
                    for analyzer in self.analyzers:
                        source = analyzer.matcher.get_source_that_meets_conditions(channel_message)
                        if source:
                            print('source = ' + str(source))
                            analyzer.executor.execute(source)
                    self.last_message_ts = channel_message['ts']
        except error.URLError as e:
            print(str(e))
