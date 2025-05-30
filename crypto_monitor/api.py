"""
API module for handling cryptocurrency data requests
"""

from .config import get_env_value
import requests

def get_crypto_price(crypto_id):
    """
    Get the current price of a cryptocurrency in USD.
    
    Args:
        crypto_id (str): The ID of the cryptocurrency
        
    Returns:
        float: The current price in USD or None if there's an error
    """
    try:
        api_url = get_env_value('API_URL', 'https://api.coingecko.com/api/v3')
        url = f"{api_url}/simple/price?ids={crypto_id}&vs_currencies=usd"
        response = requests.get(url)
        data = response.json()
        return data[crypto_id]['usd']
    except Exception as e:
        print(f"Error getting price: {e}")
        return None

def search_crypto_by_name(search_term):
    """
    Search for cryptocurrencies by name or ID.
    
    Args:
        search_term (str): The search term to look for
        
    Returns:
        list: List of matching cryptocurrencies or None if there's an error
    """
    try:
        api_url = get_env_value('API_URL', 'https://api.coingecko.com/api/v3')
        url = f"{api_url}/coins/list"
        response = requests.get(url)
        all_coins = response.json()
        
        # Convert search term to lowercase for case-insensitive search
        search_term = search_term.lower()
        
        # Search for matches in name and ID
        matches = []
        for coin in all_coins:
            if search_term in coin['name'].lower() or search_term in coin['id'].lower():
                matches.append(coin)
        
        return matches
    except Exception as e:
        print(f"Error searching for cryptocurrency: {e}")
        return None 