import json
import os

DEFAULT_CONFIG = {
    'setting_1': 'default_value_1',
    'setting_2': 'default_value_2',
    'setting_3': 10
}

def load_config(custom_config_path=None):
    """Load configuration from a JSON file, falling back to defaults."""
    config = DEFAULT_CONFIG.copy()  # Start with defaults
    
    if custom_config_path and os.path.exists(custom_config_path):
        with open(custom_config_path, 'r') as config_file:
            try:
                custom_config = json.load(config_file)
                config.update(custom_config)  # Update with custom values
            except json.JSONDecodeError as e:
                raise ValueError(f'Error loading JSON config: {e}')  
    return config
