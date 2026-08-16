import time
import random

RETRY_ATTEMPTS = 3
DELAY_SECONDS = 2

class NetworkError(Exception):
    pass

def retry_on_failure(func):
    """
    Decorator to retry a network operation if it fails.
    """
    def wrapper(*args, **kwargs):
        for attempt in range(RETRY_ATTEMPTS):
            try:
                return func(*args, **kwargs)
            except NetworkError as e:
                if attempt < RETRY_ATTEMPTS - 1:
                    time.sleep(DELAY_SECONDS * (attempt + 1))  # Exponential backoff
                else:
                    raise e
    return wrapper

@retry_on_failure
def network_operation():
    """
    Simulated network operation that may fail.
    """
    if random.choice([True, False]):
        raise NetworkError("Network failure")
    return "Network operation succeeded!"
