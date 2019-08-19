from ..contracts.DingContract import DingContract
from masonite.drivers.BaseDriver import BaseDriver


class DingPrintDriver(DingContract, BaseDriver):

    def show_message(self, message):
        print(self.get_prefix() + message)
        pass
