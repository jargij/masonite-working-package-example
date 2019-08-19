from masonite.provider import ServiceProvider

from .drivers.DingDumpDriver import DingDumpDriver
from .drivers.DingPrintDriver import DingPrintDriver
from .commands.InstallCommand import InstallCommand
from .managers.DingManager import DingManager
from config import ding


class DingServiceProvider(ServiceProvider):
    wsgi = False

    def register(self):
        self.app.bind(
            'DingInstallCommand', InstallCommand()
        )

        self.app.bind(
            'DingManager', DingManager
        )

        self.app.bind('DingPrintDriver', DingPrintDriver)
        self.app.bind('DingDumpDriver', DingDumpDriver)
        self.app.bind('DingConfig', ding)

    def boot(self, manager: DingManager):
        self.app.swap(DingManager, manager.driver(self.app.make('DingConfig').DRIVER))
