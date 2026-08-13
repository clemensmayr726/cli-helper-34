import logging

# Configure the logger settings
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('app.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

# Log a debug message
logger.debug('Debugging mode is on.')

def log_info(message: str):
    """Logs an informational message."""
    logger.info(message)


def log_warning(message: str):
    """Logs a warning message."""
    logger.warning(message)


def log_error(message: str):
    """Logs an error message."""
    logger.error(message)


def log_exception(exc: Exception):
    """Logs an exception message alongside traceback."""
    logger.exception('An error occurred', exc_info=exc)

# Example usage of logging functions
if __name__ == '__main__':
    log_info('Application started')
    try:
        1 / 0  # Intentional error
    except Exception as e:
        log_exception(e)
    log_info('Application finished')