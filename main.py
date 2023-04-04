import csv
import datetime
ACCOUNT_BALANCE = 10000
TRADES_FILE = "trades.csv"
column_headings = ['id', 'type', 'status', 'pair', 'entry_price', 'take_profit', 'stop_loss', 'expiry_date', 'quantity', 'buy_sell', 'current_price', 'timestamp', 'notes']

def add_trade(trade_type, trade_pair, entry_price, take_profit, stop_loss, expiry_date, quantity, buy_sell, notes, current_price):
    with open(TRADES_FILE, mode='a', newline='') as trades_file:
        trade_writer = csv.writer(trades_file)
        timestamp = datetime.datetime.now()
        trade_id = get_next_trade_id()
        trade_status = "ongoing"
        trade_writer.writerow([trade_id, trade_type, trade_status, trade_pair, entry_price, take_profit, stop_loss, expiry_date, quantity, buy_sell, current_price, timestamp, notes])

def exit_trade(trade_id, exit_price):
    trades = get_trades()
    for trade in trades:
        if trade[0] == str(trade_id):
            trade[2] = "ended"
            trade[5] = exit_price
            timestamp = datetime.datetime.now()
            trade.append(timestamp)
            update_trades(trades)

def get_trades():
    with open(TRADES_FILE, mode='r') as trades_file:
        trade_reader = csv.reader(trades_file)
        trades = []
        for row in trade_reader:
            trades.append(row)
        return trades

def update_trades(trades):
    with open(TRADES_FILE, mode='w', newline='') as trades_file:
        trade_writer = csv.writer(trades_file)
        trade_writer.writerows(trades)

def get_active_capital():
    trades = get_trades()
    active_capital = 0
    for trade in trades:
        if trade[2] == 'ongoing':
            quantity = float(trade[8])
            entry_price = float(trade[4])
            active_capital += quantity * entry_price
    return active_capital

def get_idle_capital(base_currency="USD"):
    trades = get_trades()
    active_capital = get_active_capital()
    idle_capital = ACCOUNT_BALANCE - active_capital
    return idle_capital

def get_next_trade_id():
    trades = get_trades()
    if len(trades) == 0:
        return 1
    else:
        last_trade_id = int(trades[-1][0])
        return last_trade_id + 1
    
def visualize_pnl(current_prices):
    trades = get_trades()
    realized_pnl = 0
    unrealized_pnl = 0
    for trade in trades:
        quantity = float(trade[8])
        entry_price = float(trade[4])
        exit_price = float(trade[5])
        if exit_price != '':
            if trade[3].startswith("USD"):
                pnl = quantity * (exit_price - entry_price)
                realized_pnl += pnl
            else:
                pnl = quantity * exit_price
                realized_pnl += pnl
        else:
            current_price = current_prices.get(trade[3])
            if trade[3].startswith("USD"):
                pnl = quantity * (current_price - entry_price)
               
add_trade("pair", "ETH/USDT", 4000, 4500, 3800, None, 10, "buy", "Bought 10 ETH at $4,000 per ETH", 4000)
