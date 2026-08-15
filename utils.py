import json
from typing import Any, Dict, List, Union

def load_json(filepath: str) -> Union[Dict, List]:
    """
    Load a JSON file and return its content as a dictionary or list.
    :param filepath: Path to the JSON file.
    :return: Parsed JSON data as a dictionary or list.
    """
    with open(filepath, 'r') as file:
        return json.load(file)


def dump_json(data: Union[Dict, List], filepath: str) -> None:
    """
    Dump data to a JSON file.
    :param data: Data to be written to file, must be a dictionary or list.
    :param filepath: Path to save the JSON file.
    """
    with open(filepath, 'w') as file:
        json.dump(data, file, indent=4)


def merge_dicts(dict1: Dict[str, Any], dict2: Dict[str, Any]) -> Dict[str, Any]:
    """
    Merge two dictionaries. In case of conflicts, values from dict2 will overwrite those from dict1.
    :param dict1: First dictionary.
    :param dict2: Second dictionary.
    :return: Merged dictionary with combined keys and values.
    """
    merged = dict1.copy()  
    merged.update(dict2)  
    return merged


def flatten_list(nested_list: List[List[Any]]) -> List[Any]:
    """
    Flatten a nested list.
    :param nested_list: List of lists to be flattened.
    :return: A single list containing all the elements.
    """
    return [item for sublist in nested_list for item in sublist]