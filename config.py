from typing import Dict, Any

class Config:
    """
    Configuration handler to manage application settings.
    """
    def __init__(self, config: Dict[str, Any]) -> None:
        """
        Initialize the configuration with the provided dictionary.
        
        :param config: A dictionary containing configuration settings.
        """
        self.config = config

    def get(self, key: str, default: Any = None) -> Any:
        """
        Retrieve the value for a configuration key.
        
        :param key: The configuration key to retrieve.
        :param default: The default value to return if the key does not exist.
        :return: The value associated with the key or default if not found.
        """
        return self.config.get(key, default)

    def set(self, key: str, value: Any) -> None:
        """
        Set a value for a configuration key.
        
        :param key: The configuration key to set.
        :param value: The value to assign to the key.
        """
        self.config[key] = value

    def all(self) -> Dict[str, Any]:
        """
        Retrieve all configuration settings.
        
        :return: A copy of the entire configuration dictionary.
        """
        return self.config.copy()