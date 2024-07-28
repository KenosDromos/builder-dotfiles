import os
from datetime import datetime


# ______________________________________________________________________ SystemInterface
class SystemInterface:
    @staticmethod
    def verify_file(file_path: str) -> bool:
        """Test whether a path exists. Returns False for broken symbolic links"""
        return os.path.exists(file_path)
    
    @staticmethod
    def rename_file(old_name: str, new_name: str) -> None:
        """Rename the file by path"""
        os.rename(old_name, new_name)

    @staticmethod
    def get_creation_time(file_path: str, *, format_time: str = '%Y-%m-%d_%H-%M-%S') -> str:
        """Returns the file creation time"""
        if SystemInterface.verify_file(file_path):
            creation_time = os.path.getctime(file_path)
            formatted_time = datetime.fromtimestamp(creation_time).strftime(format_time)
            
            return formatted_time
        else:
            raise FileNotFoundError
        
    @staticmethod
    def get_system_time(format_time: str = '%Y-%m-%d_%H-%M-%S') -> str:
        """Returns the current system time"""
        return datetime.now().strftime(format_time)