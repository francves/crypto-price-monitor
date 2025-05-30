# Crypto Price Monitor

A Python script that monitors cryptocurrency prices in real-time and alerts you when significant price changes occur.

## Features

- Real-time price monitoring using the CoinGecko API
- Configurable price change threshold for alerts
- Sound alerts when price changes exceed the threshold
- Price updates every 30 seconds
- Support for any cryptocurrency available on CoinGecko

## Requirements

- Python 3.x
- requests library

## Installation

1. Clone this repository:
```bash
git clone https://github.com/YOUR_USERNAME/crypto-price-monitor.git
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

2. By default, the script monitors Bitcoin with a 1% price change threshold. You can modify these settings in the script:
   - Change `CRYPTO_ID` to monitor a different cryptocurrency
   - Adjust `THRESHOLD_PERCENTAGE` to change the alert threshold

3. To stop monitoring, press `Ctrl+C`

## Configuration

You can modify these variables in the script:
- `CRYPTO_ID`: The ID of the cryptocurrency to monitor (e.g., "bitcoin", "ethereum", "dogecoin")
- `THRESHOLD_PERCENTAGE`: The percentage change that triggers an alert (default: 1%)

## License

This project is open source and available under the MIT License. 