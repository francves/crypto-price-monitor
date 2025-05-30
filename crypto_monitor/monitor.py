"""
Monitoring module for tracking cryptocurrency prices
"""

import time
import winsound
from datetime import datetime
from .config import get_env_value
from .api import get_crypto_price

def play_alert():
    """Play an alert sound when price changes exceed the threshold."""
    winsound.Beep(1000, 500)

def monitor_crypto(crypto_id, threshold_percentage):
    """
    Monitor a cryptocurrency's price and alert on significant changes.
    
    Args:
        crypto_id (str): The ID of the cryptocurrency to monitor
        threshold_percentage (float): The percentage change that triggers an alert
    """
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
        update_interval = get_env_value('UPDATE_INTERVAL', '30', int)
        time.sleep(update_interval) 