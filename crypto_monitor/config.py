"""
Configuration module for handling environment variables
"""

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def get_env_value(key, default, type_cast=str):
    """
    Get a value from environment variables and convert it to the specified type.
    
    Args:
        key (str): The environment variable key
        default: The default value if the key is not found
        type_cast (type): The type to convert the value to
        
    Returns:
        The converted value or the default value if conversion fails
    """
    value = os.getenv(key, default)
    # Remove any comments after the value
    if isinstance(value, str):
        value = value.split('#')[0].strip()
    try:
        return type_cast(value)
    except (ValueError, TypeError):
        print(f"Warning: Invalid value for {key}, using default: {default}")
        return type_cast(default)

# Default configuration values
DEFAULT_CONFIG = {
    'CRYPTO_ID': 'bitcoin',
    'THRESHOLD_PERCENTAGE': 0.05,
    'API_URL': 'https://api.coingecko.com/api/v3',
    'UPDATE_INTERVAL': 30
} 