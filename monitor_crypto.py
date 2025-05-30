import requests
import time
import winsound
from datetime import datetime

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

if __name__ == "__main__":
    # Configuration
    CRYPTO_ID = "bitcoin"  # You can change this to another cryptocurrency (e.g., "ethereum", "dogecoin")
    THRESHOLD_PERCENTAGE = 0.01  # Alert if price changes more than 1%
    
    try:
        monitor_crypto(CRYPTO_ID, THRESHOLD_PERCENTAGE)
    except KeyboardInterrupt:
        print("\nMonitoring stopped by user.") 