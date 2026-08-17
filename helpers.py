import os
import json
import shutil


def read_json(file_path):
    """Reads a JSON file and returns the content as a dictionary."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    with open(file_path, 'r') as file:
        return json.load(file)


def write_json(file_path, data):
    """Writes a dictionary to a JSON file."""
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)


def copy_file(src, dst):
    """Copies a file from src to dst."""
    if not os.path.exists(src):
        raise FileNotFoundError(f"The source file {src} does not exist.")
    shutil.copy(src, dst)


def delete_file(file_path):
    """Deletes the specified file if it exists."""
    if os.path.exists(file_path):
        os.remove(file_path)
    else:
        raise FileNotFoundError(f"The file {file_path} does not exist.")
