import os

from actions.executors.Executor import Executor


class WindowsVlcKiller(Executor):
    def __init__(self, config):
        self.executable = config['video-player']

    def execute(self, source):
        os.system("taskkill /im vlc.exe")
