import logging
from setup import ConfigApplication



# ______________________________________________________________________ Application
class Application:
    def __init__(self):
        self.log = logging.getLogger('root')
        self.config = ConfigApplication


    def builder(self):
        pass