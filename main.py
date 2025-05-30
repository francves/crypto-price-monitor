#!/usr/bin/env python3
"""
Main script for the cryptocurrency price monitor
"""

from crypto_monitor import (
    get_env_value,
    monitor_crypto,
    search_crypto_by_name,
    display_search_results
)

def main():
    """Main function to run the cryptocurrency monitor."""
    print("1. Monitor a cryptocurrency")
    print("2. Search cryptocurrency by name")
    option = input("\nSelect an option (1/2): ")
    
    if option == "1":
        # Configuration from environment variables with defaults
        CRYPTO_ID = get_env_value('CRYPTO_ID', 'bitcoin')
        THRESHOLD_PERCENTAGE = get_env_value('THRESHOLD_PERCENTAGE', '0.05', float)
        
        try:
            monitor_crypto(CRYPTO_ID, THRESHOLD_PERCENTAGE)
        except KeyboardInterrupt:
            print("\nMonitoring stopped by user.")
    
    elif option == "2":
        search_term = input("\nEnter cryptocurrency name to search: ")
        matches = search_crypto_by_name(search_term)
        display_search_results(matches)
        
        if matches:
            print("\nTo monitor one of these cryptocurrencies, copy its ID and use it in the script.")
            print("You can modify the CRYPTO_ID variable in the .env file with the desired ID.")
    
    else:
        print("Invalid option")

if __name__ == "__main__":
    main() 