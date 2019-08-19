from abc import ABC, abstractmethod
from config import ding


class DingContract(ABC):
    message = ""
    configuration = {}
    prefix = ""

    def __init__(self):
        self.configuration = ding.DRIVERS[ding.DRIVER]
        pass

    def get_prefix(self):
        return self.configuration.get('prefix', 'No prefix found: ')

    @abstractmethod
    def show_message(self, message):
        self.message = message
        pass
