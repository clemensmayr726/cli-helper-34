import logging
import os
from logging.handlers import RotatingFileHandler

def setup_logger(log_file='app.log', max_bytes=10*1024*1024, backup_count=3):
    logger = logging.getLogger('my_logger')
    logger.setLevel(logging.DEBUG)

    # Create a rotating file handler
    os.makedirs(os.path.dirname(log_file), exist_ok=True)
    handler = RotatingFileHandler(log_file, maxBytes=max_bytes, backupCount=backup_count)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    # Add the handler to the logger
    logger.addHandler(handler)
    return logger

# Example usage
if __name__ == '__main__':
    logger = setup_logger()
    logger.info('Logger setup complete.')