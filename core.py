import json
from typing import Any, Dict, List

def load_json(file_path: str) -> Dict[str, Any]:
    """
    Load a JSON file and return its content as a dictionary.
    :param file_path: Path to the JSON file.
    :return: Dictionary containing the JSON data.
    """
    with open(file_path, 'r') as file:
        return json.load(file)


def save_json(file_path: str, data: Dict[str, Any]) -> None:
    """
    Save data as a JSON file.
    :param file_path: Path where to save the JSON file.
    :param data: Dictionary to save as JSON.
    """
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)


def merge_dicts(dict1: Dict[str, Any], dict2: Dict[str, Any]) -> Dict[str, Any]:
    """
    Merge two dictionaries and return the result.
    :param dict1: The first dictionary.
    :param dict2: The second dictionary.
    :return: Merged dictionary.
    """
    merged = dict1.copy()
    merged.update(dict2)
    return merged


def flatten_list_of_dicts(list_of_dicts: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    Flatten a list of dictionaries into a single dictionary per unique key.
    :param list_of_dicts: List of dictionaries to flatten.
    :return: A flattened list of dictionaries.
    """
    result = []
    for d in list_of_dicts:
        result.append({k: v for k, v in d.items()})
    return result