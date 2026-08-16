import json
import os
from typing import Any, Dict

DEFAULT_CONFIG = {
    'host': 'localhost',
    'port': 8080,
    'debug': False
}

class ConfigLoader:
    def __init__(self, config_file: str) -> None:
        self.config_file = config_file
        self.config = self.load_config()

    def load_config(self) -> Dict[str, Any]:
        # Load configuration from JSON file; fallback to defaults
        if os.path.isfile(self.config_file):
            with open(self.config_file, 'r') as file:
                user_config = json.load(file)
                return {**DEFAULT_CONFIG, **user_config}
        return DEFAULT_CONFIG

    def get(self, key: str, default: Any = None) -> Any:
        return self.config.get(key, default)

    def __repr__(self) -> str:
        return f"ConfigLoader(config={self.config})"

if __name__ == '__main__':
    config_loader = ConfigLoader('config.json')
    print(config_loader)