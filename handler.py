import json
import logging

class CustomError(Exception):
    pass

def process_data(data):
    if not isinstance(data, dict):
        raise CustomError('Input must be a dictionary')
    if 'key' not in data:
        raise CustomError('Missing key in input data')
    return data['key'] * 2

def main():
    logging.basicConfig(level=logging.ERROR)
    test_data = [{'key': 5}, {'key': 10}, {'wrong_key': 20}, 'not a dict']
    results = []

    for item in test_data:
        try:
            result = process_data(item)
            results.append(result)
        except CustomError as e:
            logging.error(f'Error processing item {item}: {e}')

    print(json.dumps({'results': results}, indent=2))

if __name__ == '__main__':
    main() 