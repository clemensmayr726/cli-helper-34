import json
from typing import Any, Union, List, Dict

class DataHandler:
    @staticmethod
    def load_json(file_path: str) -> Union[Dict[str, Any], List[Any]]:
        """Load JSON data from a file."""
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)

    @staticmethod
    def save_json(data: Union[Dict[str, Any], List[Any]], file_path: str) -> None:
        """Save data to a JSON file."""
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    @staticmethod
    def merge_data(data1: Union[Dict[str, Any], List[Any]], data2: Union[Dict[str, Any], List[Any]]) -> Union[Dict[str, Any], List[Any]]:
        """Merge two data collections."""
        if isinstance(data1, dict) and isinstance(data2, dict):
            return {**data1, **data2}
        elif isinstance(data1, list) and isinstance(data2, list):
            return data1 + data2
        raise ValueError('Both inputs must be of the same type (dict or list)')

    @staticmethod
    def filter_data(data: List[Dict[str, Any]], key: str, value: Any) -> List[Dict[str, Any]]:
        """Filter a list of dictionaries based on a key-value pair."""
        return [item for item in data if item.get(key) == value]
