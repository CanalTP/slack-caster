import re


class YoutubeMatcher:
    def get_source_that_meets_conditions(self, channel_message):
        if channel_message['type'] == 'message' and \
                ('attachments' in channel_message and len(channel_message['attachments']) > 0 and
                         channel_message['attachments'][0]['service_name'] == 'YouTube'):
            return channel_message['attachments'][0]['from_url']
        if re.match(
                '^<?((?:https?:)?\/\/)?((?:www|m)\.)?((?:youtube\.com|youtu.be))(\/(?:[\w\-]+\?v=|embed\/|v\/)?)([\w\-]+)(\S+)?>?$',
                channel_message['text']):
            url_to_read = channel_message['text']
            for match in ['<', '>', '\\']:
                url_to_read = url_to_read.replace(match, '')
            return url_to_read
