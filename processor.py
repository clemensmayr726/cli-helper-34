import json
import logging
from typing import Any, Dict

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ProcessingError(Exception):
    pass

def process_data(data: Dict[str, Any]) -> Dict[str, Any]:
    if not isinstance(data, dict):
        logger.error('Data must be a dictionary')
        raise ProcessingError('Invalid data format: expected dictionary.')
    if 'value' not in data:
        logger.error('Missing required key: value')
        raise ProcessingError('Missing required key: value.')
    value = data['value']
    if not isinstance(value, (int, float)):
        logger.error('Value must be an int or float')
        raise ProcessingError('Invalid value type: expected int or float.')
    # Simulate processing
    processed_value = value * 2  # Example processing
    return {'processed_value': processed_value}

if __name__ == '__main__':
    try:
        sample_data = json.loads('{"value": 5}')  # Sample input
        result = process_data(sample_data)
        print(result)
    except ProcessingError as e:
        logger.exception('Processing failed: %s', str(e))
    except json.JSONDecodeError:
        logger.exception('Failed to decode JSON input')
    except Exception as e:
        logger.exception('An unexpected error occurred: %s', str(e))
