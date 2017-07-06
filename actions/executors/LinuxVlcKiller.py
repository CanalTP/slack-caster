import os
import signal
import subprocess

from actions.executors.Executor import Executor


class LinuxVlcKiller(Executor):

    def __init__(self, config):
        self.executable = config['video-player']

    def execute(self, source):
        out, err = subprocess.Popen(['ps', '-A'], stdout=subprocess.PIPE, universal_newlines=True).communicate()
        for line in out.splitlines():
            if self.executable in line:
                print('killing vlc')
                os.kill(int(line.split(None, 1)[0]), signal.SIGKILL)
