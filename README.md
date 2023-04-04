# Python Trading Log
This Python script is designed to help you log your trades and keep track of your P&L. The script stores the trades in a CSV file and provides several functions to interact with the data. You can use this script to log trades across multiple trading strategies, including spot trades, futures, options, and prediction markets.


## Usage
### Logging Trades
Adding a Trade
To add a trade, you can call the add_trade function and pass in the following parameters:

- trade_type: The type of trade, such as "spot", "margin", or "option".
- trade_pair: The trading pair, such as "BTC/USD" or "ETH/BTC".
- entry_price: The entry price for the trade.
- take_profit: The take profit price for the trade.
- stop_loss: The stop loss price for the trade.
- expiry_date: The expiry date for the trade, if applicable.
- quantity: The quantity of the asset being traded.
- buy_sell: Whether the trade is a buy or a sell.
- notes: Any notes or comments about the trade.
- current_price: The current market price for the asset being traded.

```
from trade_logger import add_trade

add_trade("spot", "BTC/USD", 50000, 55000, 48000, "", 1, "buy", "Long BTC", 49500)
```

### Exiting a Trade

To exit a trade, you can call the exit_trade function and pass in the trade ID and the exit price.

```
from trade_logger import exit_trade

exit_trade(1, 52000)
```

### Visualizing P&L
To visualize your P&L, you can call the visualize_pnl function. This function takes in a dictionary of current prices for the assets being traded.

```
from trade_logger import visualize_pnl

current_prices = {"BTC/USD": 54000, "ETH/BTC": 0.034}
visualize_pnl(current_prices)
```

### Getting Active Capital
To get the amount of active capital you have tied up in ongoing trades, you can call the get_active_capital function.

```
from trade_logger import get_active_capital

active_capital = get_active_capital()
print(f"Active capital: {active_capital}")
```

### Getting Idle Capital
To get the amount of idle capital you have available from ended trades, you can call the get_idle_capital function.

```
from trade_logger import get_idle_capital

idle_capital = get_idle_capital()
print(f"Idle capital: {idle_capital}")
```

### Getting Active Capital per Strategy
To get the amount of active capital you have tied up in ongoing trades per strategy, you can call the get_active_capital_per_strategy function.

```
from trade_logger import get_active_capital_per_strategy

active_capital_per_strategy = get_active_capital_per_strategy()
print("Active capital per strategy:")
for strategy, capital in active_capital_per_strategy.items():
    print(f"{strategy}: {capital}")
```

### Visualizing P&L
To visualize the P&L of all trades, use the visualize_pnl() function. This function takes a dictionary of current prices as an argument, which is used to calculate the unrealized P&L of ongoing trades. The current prices should be in the same format as the trade_pair column in the trades.csv file.

```
current_prices = {
    "BTC/USD": 50000,
    "ETH/USD": 1500,
    "ADA/BTC": 0.00002,
    "LINK/ETH": 0.03,
    "Bored Apes": 0.6
}

visualize_pnl(current_prices)
```

This will print out the realized P&L and unrealized P&L of all trades.

## Conclusion

This script provides a basic framework for logging and managing trades in Python. It can be customized to suit your needs and extended with additional functionality. With this script, you can easily keep track of your trades, calculate your P&L, and monitor your active and idle capital.