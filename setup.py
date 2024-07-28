import logging


from builder.modules.system import SystemInterface



# ______________________________________________________________________ LoggerConfigurator
class LoggerConfigurator:
    """Class for configuring logger settings"""
    
    def __init__(self, dir: str = "builder/logs/", filename: str = "lates.log"):
        self.dir = dir
        self.filename = filename
        self.path = self.dir + self.filename

        self._rename_last_file()
        self._configuration_logging()
        
    def _rename_last_file(self):
        """Renames the last log file"""
        old_file_path = self.path

        if SystemInterface.verify_file(old_file_path):
            creation_time = SystemInterface.get_creation_time(old_file_path, format_time="%Y-%m-%d")
            index_log = 0

            while True:
                new_file_path = self.dir + f"{creation_time}_{index_log}.log"
                index_log += 1

                if not SystemInterface.verify_file(new_file_path):
                    SystemInterface.rename_file(old_file_path, new_file_path)
                    break

    def _configuration_logging(self):
        """Configuring the basic configuration file of the logging package"""
        formatter = '%(asctime)s | %(filename)-18s %(levelname)-8s: %(message)s'

        logging.basicConfig(filename=self.path, encoding='utf-8', level=logging.DEBUG, format=formatter)


# ______________________________________________________________________ BuilderConfigurator
class BuilderConfigurator:
    """Class for configuring builder settings"""

    def __init__(self, dir: str = "config/", filename: str = "builder_config.json"):
        self.dir = dir
        self.filename = filename
        self.path = self.dir + self.filename


# ______________________________________________________________________ Setup
class ConfigApplication:
    """Configures all application modules"""
    launch = True
    
    logger: LoggerConfigurator
    builder: BuilderConfigurator

    @staticmethod
    def start():
        """Start configuring all modules. Launch at the beginning of the application"""
        if ConfigApplication.launch:
            ConfigApplication.logger = LoggerConfigurator()
            ConfigApplication.builder = BuilderConfigurator()

            ConfigApplication.launch = False
    
    


