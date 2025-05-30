# Crypto Price Monitor

A Python script that monitors cryptocurrency prices in real-time and alerts you when significant price changes occur.

## Features

- Real-time price monitoring using the CoinGecko API
- Search cryptocurrencies by name to find their IDs
- Configurable price change threshold for alerts (default: 5%)
- Sound alerts when price changes exceed the threshold
- Price updates every 30 seconds
- Support for any cryptocurrency available on CoinGecko

## Requirements

- Python 3.x
- requests library

## Installation

1. Clone this repository:
```bash
git clone https://github.com/francves/crypto-price-monitor.git
cd crypto-price-monitor
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Run the script:
```bash
python monitor_crypto.py
```

2. Choose an option:
   - Option 1: Monitor a cryptocurrency
   - Option 2: Search for a cryptocurrency by name

### Monitoring a Cryptocurrency

When you select option 1, the script will:
- Monitor the specified cryptocurrency (default: Bitcoin)
- Display the current price every 30 seconds
- Alert you with a sound when the price changes by more than the threshold
- Show the percentage change when an alert is triggered

### Searching for Cryptocurrencies

When you select option 2, you can:
- Enter a cryptocurrency name to search
- View a list of matching cryptocurrencies with their IDs
- Use the found ID to monitor a specific cryptocurrency

## Configuration

You can modify these variables in the script:
- `CRYPTO_ID`: The ID of the cryptocurrency to monitor (e.g., "bitcoin", "ethereum", "dogecoin")
- `THRESHOLD_PERCENTAGE`: The percentage change that triggers an alert (default: 5%)

## Examples

1. To monitor Bitcoin:
```python
CRYPTO_ID = "bitcoin"
THRESHOLD_PERCENTAGE = 0.05  # 5% change
```

2. To monitor Ethereum:
```python
CRYPTO_ID = "ethereum"
THRESHOLD_PERCENTAGE = 0.05  # 5% change
```

## License

This project is open source and available under the MIT License. 