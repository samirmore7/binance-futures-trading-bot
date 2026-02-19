# binance-futures-trading-bot
# Binance Futures Testnet Trading Bot

A Python CLI application that places MARKET and LIMIT orders on Binance Futures Testnet (USDT-M) with structured architecture, validation, logging, and error handling.

## Features

- Market and Limit order placement
- BUY and SELL support
- CLI-based input (argparse)
- Logging of API requests and responses
- Exception handling
- Modular code structure

## Setup

1. Clone repository
2. Create virtual environment

python -m venv venv
venv\Scripts\activate

3. Install dependencies

pip install -r requirements.txt

4. Add API keys in `.env`

API_KEY=your_key  
API_SECRET=your_secret  

## Usage

### MARKET order

python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.003

### LIMIT order

python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.003 --price 65000

## Logs

All requests and responses are stored in `logs.log`.

## Assumptions

- Futures testnet account active
- Valid API keys
- Minimum notional requirements followed
