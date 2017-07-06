import os

from actions.executors.VlcExecutor import VlcExecutor


class WindowsVlcExecutor(VlcExecutor):
    def __init__(self, config):
        self.executable = config['video-player']
        if str(os.sep) in self.executable:
            exec_parts = self.executable.split(os.sep)
            executable_dir = os.sep.join(exec_parts[:-1])
            print("chdir to " + executable_dir)
            os.chdir(executable_dir)
            self.executable = exec_parts[-1:]
