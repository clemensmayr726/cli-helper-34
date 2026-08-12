import json

class CustomError(Exception):
    pass

def risky_operation(data):
    if not isinstance(data, dict):
        raise CustomError('Input must be a dictionary')
    if 'key' not in data:
        raise CustomError('Key not found in input dictionary')
    return data['key']

def process_data(json_data):
    try:
        data = json.loads(json_data)
        result = risky_operation(data)
        print(f'Processed result: {result}')
    except json.JSONDecodeError:
        print('Error: Invalid JSON format')
    except CustomError as e:
        print(f'Custom Error: {e}')
    except Exception as e:
        print(f'Unexpected Error: {e}')

if __name__ == '__main__':
    sample_json = '{"key": "value"}'
    process_data(sample_json)