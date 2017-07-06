from subprocess import call


class VlcExecutor:
    def execute(self, source):
        print('execute ' + self.executable)
        call([self.executable, '--play-and-exit', source])
