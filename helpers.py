from typing import List, Dict


def sort_dict_by_value(input_dict: Dict[str, int]) -> List[Dict[str, int]]:
    """
    Sorts a dictionary by its values in descending order.
    
    Args:
        input_dict (Dict[str, int]): The dictionary to be sorted.
    
    Returns:
        List[Dict[str, int]]: A list of dictionaries sorted by value.
    """
    return sorted(input_dict.items(), key=lambda item: item[1], reverse=True)


def filter_even_numbers(numbers: List[int]) -> List[int]:
    """
    Filters out even numbers from a list.
    
    Args:
        numbers (List[int]): The list of integers to be filtered.
    
    Returns:
        List[int]: A list containing only the even numbers.
    """
    return [num for num in numbers if num % 2 == 0]


def merge_dicts(dict1: Dict[str, str], dict2: Dict[str, str]) -> Dict[str, str]:
    """
    Merges two dictionaries into one. If the same key exists in both, the value from dict2 is taken.
    
    Args:
        dict1 (Dict[str, str]): The first dictionary.
        dict2 (Dict[str, str]): The second dictionary.
    
    Returns:
        Dict[str, str]: The merged dictionary.
    """
    merged = dict1.copy()
    merged.update(dict2)
    return merged
