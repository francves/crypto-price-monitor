"""
Crypto Monitor - A cryptocurrency price monitoring tool
"""

from .config import get_env_value
from .api import get_crypto_price, search_crypto_by_name
from .monitor import monitor_crypto, play_alert
from .display import display_search_results

__version__ = '1.0.0'

# Export all necessary functions
__all__ = [
    'get_env_value',
    'get_crypto_price',
    'search_crypto_by_name',
    'monitor_crypto',
    'play_alert',
    'display_search_results'
] 