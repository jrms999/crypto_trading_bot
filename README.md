# crypto_trading_bot
This version supports Binance and runs a simple moving average crossover strategy.

- Back-end logic (Python using ccxt for exchange API access)
- Front-end (for monitoring via a browser)

💡 Features for This Bot (Starter Version)
- Supports Binance (can be extended to other exchanges)
- Uses Python and ccxt to connect to the exchange
- Strategy: Simple Moving Average Crossover
- Buys when short-term MA crosses above long-term MA (bullish)
- Sells when short-term MA crosses below long-term MA (bearish)
- Logging and balance tracking
- Run interval: Every X seconds (configurable)

Next push - 
- Add a dashboard (web frontend) to monitor it
- Extend it to more exchanges or altcoins
- Include Telegram or email notifications
- Use advanced strategies (RSI, MACD, etc.)
