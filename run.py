from setup import ConfigApplication
from builder.app import Application
from builder.modules.system import SystemInterface

import os

def main():
    ConfigApplication.start()
    
    # app = Application()


if "__main__" == __name__:
    main()