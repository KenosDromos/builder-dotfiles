from 

import logging


class LoggerConfigurator:
    """
    Class for configuring logger settings.
    """
    
    def __init__(self) -> None:
        """
        Initialize LoggerConfigurator with default parameters.
        """
        log_dir = "installer-dotfiles/logs/"
        filename_prefix = "install"

        date = '%Y-%m-%d_%T:%T:%Z'
        filename = f"{filename_prefix}_{date}.log"

        formatter = '%(asctime)s | %(filename)-18s %(levelname)-8s: %(message)s'
        logging.basicConfig(filename=(log_dir + filename), encoding='utf-8', level=logging.DEBUG, format=formatter)


class Setup:
    @staticmethod
    def 


