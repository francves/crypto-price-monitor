# Crypto Price Monitor

A Python script that monitors cryptocurrency prices in real-time and alerts you when significant price changes occur.

## Features

- Real-time price monitoring using the CoinGecko API
- Search cryptocurrencies by name to find their IDs
- Configurable price change threshold for alerts (default: 5%)
- Sound alerts when price changes exceed the threshold
- Price updates every 30 seconds
- Support for any cryptocurrency available on CoinGecko
- Environment-based configuration

## Requirements

- Python 3.x
- requests library
- python-dotenv library

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

3. Configure your environment:
   - Copy `.env.example` to `.env`
   - Modify the values in `.env` according to your needs

## Configuration

The script can be configured using environment variables in the `.env` file:

```env
# Cryptocurrency Configuration
CRYPTO_ID=bitcoin              # ID of the cryptocurrency to monitor
THRESHOLD_PERCENTAGE=0.05      # Alert threshold (5%)

# API Configuration
API_URL=https://api.coingecko.com/api/v3

# Monitoring Configuration
UPDATE_INTERVAL=30            # Update interval in seconds
```

You can find the correct cryptocurrency ID using the search option in the script.

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

## Examples

1. To monitor Bitcoin with a 5% threshold:
```env
CRYPTO_ID=bitcoin
THRESHOLD_PERCENTAGE=0.05
```

2. To monitor Ethereum with a 2% threshold:
```env
CRYPTO_ID=ethereum
THRESHOLD_PERCENTAGE=0.02
```

## License

This project is open source and available under the MIT License. 