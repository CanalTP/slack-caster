from abc import ABCMeta, abstractmethod


class Executor(metaclass=ABCMeta):
    @abstractmethod
    def execute(self, source):
        pass
