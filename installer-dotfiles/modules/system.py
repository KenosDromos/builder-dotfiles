import os

class SystemInterface:
    @staticmethod
    def verify_file(path: str) -> bool:
        """Test whether a path exists. Returns False for broken symbolic links"""
        return os.path.exists()
    