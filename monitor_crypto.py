import requests
import time
import winsound
from datetime import datetime

def search_crypto_by_name(search_term):
    try:
        url = "https://api.coingecko.com/api/v3/coins/list"
        response = requests.get(url)
        all_coins = response.json()
        
        # Convertir el término de búsqueda a minúsculas para una búsqueda insensible a mayúsculas
        search_term = search_term.lower()
        
        # Buscar coincidencias en nombre e ID
        matches = []
        for coin in all_coins:
            if search_term in coin['name'].lower() or search_term in coin['id'].lower():
                matches.append(coin)
        
        return matches
    except Exception as e:
        print(f"Error searching for cryptocurrency: {e}")
        return None

def get_crypto_price(crypto_id):
    try:
        url = f"https://api.coingecko.com/api/v3/simple/price?ids={crypto_id}&vs_currencies=usd"
        response = requests.get(url)
        data = response.json()
        return data[crypto_id]['usd']
    except Exception as e:
        print(f"Error getting price: {e}")
        return None

def play_alert():
    # Play alert sound (frequency 1000Hz, duration 500ms)
    winsound.Beep(1000, 500)

def monitor_crypto(crypto_id, threshold_percentage):
    previous_price = None
    
    print(f"Monitoring {crypto_id.upper()}...")
    print("Press Ctrl+C to stop monitoring")
    
    while True:
        current_price = get_crypto_price(crypto_id)
        
        if current_price is None:
            print("Could not get price. Retrying in 30 seconds...")
            time.sleep(30)
            continue
            
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{timestamp}] Current price: ${current_price:.2f}")
        
        if previous_price is not None:
            percentage_change = ((current_price - previous_price) / previous_price) * 100
            
            if abs(percentage_change) >= threshold_percentage:
                message = "RISE" if percentage_change > 0 else "DROP"
                print(f"ALERT! {message} of {abs(percentage_change):.2f}%")
                play_alert()
        
        previous_price = current_price
        time.sleep(30)

def display_search_results(matches):
    if not matches:
        print("No cryptocurrencies found matching your search.")
        return
    
    print("\nFound cryptocurrencies:")
    print("-" * 50)
    for coin in matches:
        print(f"Name: {coin['name']:<20} ID: {coin['id']}")
    print("-" * 50)

if __name__ == "__main__":
    print("1. Monitor a cryptocurrency")
    print("2. Search cryptocurrency by name")
    option = input("\nSelect an option (1/2): ")
    
    if option == "1":
        # Configuration
        CRYPTO_ID = "bitcoin"  # You can change this to another cryptocurrency (e.g., "ethereum", "dogecoin")
        THRESHOLD_PERCENTAGE = 0.05  # Alert if price changes more than 5%
        
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
            print("You can modify the CRYPTO_ID variable in the script with the desired ID.")
    
    else:
        print("Invalid option") 