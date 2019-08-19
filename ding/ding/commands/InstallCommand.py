import os
from cleo import Command
from masonite.packages import create_or_append_config
from ..integration import package_directory


class InstallCommand(Command):
    """
    Install Masonite Billing
    install:ding
    """

    def handle(self):
        create_or_append_config(
            os.path.join(
                package_directory,
                '../ding/snippets/configs/ding.py'
            )
        )
