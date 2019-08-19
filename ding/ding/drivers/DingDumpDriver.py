from masonite.drivers import BaseDriver
from ..contracts.DingContract import DingContract


class DingDumpDriver(DingContract, BaseDriver):

    def show_message(self, message):
        dd(self.get_prefix() + message)
        pass
