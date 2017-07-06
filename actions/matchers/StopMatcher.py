class StopMatcher:
    def get_source_that_meets_conditions(self, channel_message):
        return 'stop' in channel_message['text'].lower()
