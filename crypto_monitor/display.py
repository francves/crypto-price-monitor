"""
Display module for formatting and showing information to the user
"""

def display_search_results(matches):
    """
    Display the results of a cryptocurrency search.
    
    Args:
        matches (list): List of matching cryptocurrencies
    """
    if not matches:
        print("No cryptocurrencies found matching your search.")
        return
    
    print("\nFound cryptocurrencies:")
    print("-" * 50)
    for coin in matches:
        print(f"Name: {coin['name']:<20} ID: {coin['id']}")
    print("-" * 50) 