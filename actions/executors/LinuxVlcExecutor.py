from actions.executors.VlcExecutor import VlcExecutor


class LinuxVlcExecutor(VlcExecutor):

    def __init__(self, config):
        self.executable = config['video-player']
