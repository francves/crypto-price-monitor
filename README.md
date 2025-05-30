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
- Modular and maintainable code structure

## Project Structure

```
crypto-price-monitor/
├── crypto_monitor/          # Main package
│   ├── __init__.py         # Package initialization and exports
│   ├── api.py              # API interaction with CoinGecko
│   ├── config.py           # Environment and configuration handling
│   ├── display.py          # Results formatting and display
│   └── monitor.py          # Price monitoring logic
├── main.py                 # Main script entry point
├── requirements.txt        # Project dependencies
├── .env.example           # Example environment configuration
└── README.md              # This file
```

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
python main.py
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

## Module Documentation

### crypto_monitor.api
Handles all interactions with the CoinGecko API:
- `get_crypto_price()`: Get current price of a cryptocurrency
- `search_crypto_by_name()`: Search cryptocurrencies by name or ID

### crypto_monitor.config
Manages configuration and environment variables:
- `get_env_value()`: Get and parse environment variables
- `DEFAULT_CONFIG`: Default configuration values

### crypto_monitor.monitor
Contains the core monitoring functionality:
- `monitor_crypto()`: Main monitoring loop
- `play_alert()`: Sound alert function

### crypto_monitor.display
Handles the formatting and display of information:
- `display_search_results()`: Format and show search results

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

## Contributing

Feel free to submit issues and enhancement requests!

## License

This project is open source and available under the MIT License. 