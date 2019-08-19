from pydoc import locate

from masonite.managers import Manager
from config import ding


class DingManager(Manager):
    config = 'Dingconfig'
    driver_prefix = 'Ding'




