import sys
import logging
from networksecurity.utils import logger  # 👈 this line triggers logging setup

# Now you can use logging
logger = logging.getLogger(__name__)

class NetworkSecurityException(Exception):
    def __init__(self, error_message, error_details: sys):
        super().__init__(error_message)
        self.error_message = error_message

        _, _, exc_tb = error_details.exc_info()
        self.lineno = exc_tb.tb_lineno if exc_tb else None
        self.file_name = exc_tb.tb_frame.f_code.co_filename if exc_tb else "Unknown"

        # Automatically log the error
        logger.error(str(self))

    def __str__(self):
        return (
            f"Error occurred in script [{self.file_name}] "
            f"at line [{self.lineno}] with message: {self.error_message}"
        )

if __name__ == '__main__':
    try:
        logger.info("Entered try block")
        a = 1 / 0
    except Exception as e:
        raise NetworkSecurityException(e, sys)
