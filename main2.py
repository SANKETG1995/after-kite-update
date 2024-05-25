from kite_trade import KiteApp
import time
import pandas as pd
import winsound
from kiteconnect import KiteTicker
import re


# Read variables from 'variables.txt'
with open('variables.txt', 'r') as file:
    for line in file:
        exec(line)

# Initialize kite and retrieve user_id
enctoken = enc_token
instrument_token = code
kite = KiteApp(enctoken=enctoken)
user_id = kite.profile()["user_id"]
kws = KiteTicker(api_key="TradeViaPython", access_token=f"{enctoken}&user_id={user_id}")


stock = stock_name  # Read from variables.txt
qty = quantity  # Read from variables.txt
symbol = stock.replace('NSE:', '')


# Define callbacks
def on_ticks(ws, ticks):
    for tick in ticks:
        #print(f"{tick['last_price']}")
        global sanket_variable 
        sanket_variable = tick['last_price']

def on_connect(ws, response):
    print("Connected to WebSocket")
    # Subscribe to a list of instrument_tokens
    tokens = [instrument_token]  # Replace with the instrument tokens you need
    ws.subscribe(tokens)
    ws.set_mode(ws.MODE_LTP, tokens)  # Set mode to receive LTP updates

def on_close(ws, code, reason):
    print("Connection closed", code, reason)

def on_error(ws, code, reason):
    print("Error occurred", code, reason)

def on_reconnect(ws, attempts_count):
    print(f"Reconnecting: {attempts_count}")

# Assign the callbacks to the KiteTicker instance
kws.on_ticks = on_ticks
kws.on_connect = on_connect
kws.on_close = on_close
kws.on_error = on_error
kws.on_reconnect = on_reconnect

# Connect to WebSocket in a threaded mode
kws.connect(threaded=True)

# Wait for the connection to be established
while not kws.is_connected():
    pass
    
    #print("WebSocket connection established")

#child_function()  # This will print the last traded price if it has been updated by the WebSocket

def case1():
    print(kite.margins(), '\n')
    q = kite.margins()
    print("Profit is --->", q['equity']['utilised']['m2m_realised'])
    print("Test Profit is --->", q['equity']['available']['live_balance'])
    print("Test Profit is --->", q['equity']['available']['opening_balance'])
    
    profit = q['equity']['available']['live_balance'] - q['equity']['available']['opening_balance']
    print("Test Profitttttt --->", profit)

    # Define callbacks
    def on_ticks(ws, ticks):
        for tick in ticks:
            print(f"{tick['last_price']}")
    
    def on_connect(ws, response):
        print("Connected to WebSocket")
        # Subscribe to a list of instrument_tokens
        tokens = [instrument_token]  # Replace with the instrument tokens you need
        ws.subscribe(tokens)
        ws.set_mode(ws.MODE_LTP, tokens)  # Set mode to receive LTP updates
    
    def on_close(ws, code, reason):
        print("Connection closed", code, reason)
    
    def on_error(ws, code, reason):
        print("Error occurred", code, reason)
    
    def on_reconnect(ws, attempts_count):
        print(f"Reconnecting: {attempts_count}")
    
    # Assign the callbacks to the KiteTicker instance
    kws.on_ticks = on_ticks
    kws.on_connect = on_connect
    kws.on_close = on_close
    kws.on_error = on_error
    kws.on_reconnect = on_reconnect
    
    # Connect to WebSocket in a threaded mode
    kws.connect(threaded=True)
    
    # Wait for the connection to be established
    while not kws.is_connected():
        pass
    
    print("WebSocket connection established")

def case2():
    trailing_percent = 0.0035  # 1% trailing stop
    q = kite.margins()
    df = sanket_variable
    current_price = sanket_variable
    profit = q['equity']['available']['live_balance'] - q['equity']['available']['opening_balance']
    

    pivot_stop_price = current_price * (1 - trailing_percent)
    new_pivot = pivot_stop_price
    while current_price > pivot_stop_price:
        if current_price > pivot_stop_price:
            new_pivot = current_price * (1 - trailing_percent)
            if new_pivot > pivot_stop_price:
                pivot_stop_price = new_pivot
        df = sanket_variable
        current_price = sanket_variable
        print(f"Current Price: {current_price:.2f}, Trailing Stop Price: {pivot_stop_price:.2f}", '\n')
        print("Profit is -> ", profit, '\n')
        print("Don't eat full fish, exit after profit is -> ", 0.15 * q['equity']['available']['opening_balance'], '\n')
        time.sleep(2)
    print("Stop Loss Executed!!")
    order = kite.place_order(variety=kite.VARIETY_REGULAR,
                             exchange=kite.EXCHANGE_NSE,
                             tradingsymbol=symbol,
                             transaction_type=kite.TRANSACTION_TYPE_SELL,
                             quantity=qty,
                             product=kite.PRODUCT_MIS,
                             order_type=kite.ORDER_TYPE_MARKET,
                             price=None,
                             validity=None,
                             disclosed_quantity=None,
                             trigger_price=None,
                             squareoff=None,
                             stoploss=None,
                             trailing_stoploss=None,
                             tag="TradeViaPython")
    print(order)

def case3(): 
    # Usage example
    child_function()  # This will print the last traded price if it has been updated by the WebSocket

def case4():
    kite.modify_order(variety=kite.VARIETY_REGULAR,
                      order_id="order_id",
                      parent_order_id=None,
                      quantity=5,
                      price=200,
                      order_type=kite.ORDER_TYPE_LIMIT,
                      trigger_price=None,
                      validity=kite.VALIDITY_DAY,
                      disclosed_quantity=None)

def case5():
    order = kite.place_order(variety=kite.VARIETY_REGULAR,
                             exchange=kite.EXCHANGE_NSE,
                             tradingsymbol="estACC",
                             transaction_type=kite.TRANSACTION_TYPE_BUY,
                             quantity=1,
                             product=kite.PRODUCT_MIS,
                             order_type=kite.ORDER_TYPE_LIMIT,
                             price=3000,
                             validity=None,
                             disclosed_quantity=None,
                             trigger_price=None,
                             squareoff=None,
                             stoploss=None,
                             trailing_stoploss=None,
                             tag="TradeViaPython")
    print(order)

def case6():
    trailing_percent = 0.0035  # 1% trailing stop
    q = kite.margins()
    df = sanket_variable
    current_price = sanket_variable
    entry_price = current_price
    
    profit = q['equity']['available']['live_balance'] - q['equity']['available']['opening_balance']

    pivot_stop_price = entry_price * (1 + trailing_percent)
    new_pivot = pivot_stop_price
    while current_price < pivot_stop_price:
        if current_price < pivot_stop_price:
            new_pivot = current_price * (1 + trailing_percent)
            if new_pivot < pivot_stop_price:
                pivot_stop_price = new_pivot
        df = sanket_variable
        current_price = df
        print(f"Current Price: {current_price:.2f}, Trailing Stop Price: {pivot_stop_price:.2f}", '\n')
        print("Profit is -> ", profit, '\n')
        print("Don't eat full fish, exit after profit is -> ", 0.15 * q['equity']['available']['opening_balance'], '\n')
        time.sleep(2)
    print("Stop Loss Executed!!")
    order = kite.place_order(variety=kite.VARIETY_REGULAR,
                             exchange=kite.EXCHANGE_NSE,
                             tradingsymbol=symbol,
                             transaction_type=kite.TRANSACTION_TYPE_BUY,
                             quantity=qty,
                             product=kite.PRODUCT_MIS,
                             order_type=kite.ORDER_TYPE_MARKET,
                             price=None,
                             validity=None,
                             disclosed_quantity=None,
                             trigger_price=None,
                             squareoff=None,
                             stoploss=None,
                             trailing_stoploss=None,
                             tag="TradeViaPython")
    print(order)
    
def exit_program():
    print("Exiting the program")
    exit()

# Create a dictionary to map cases to functions
switch = {
    1: case1,
    2: case2,
    3: case3,
    4: case4,
    5: case5,
    6: case6,
    0: exit_program
}

while True:
    # Get the user's choice
    choice = int(input("Enter a case (1-6) \n2. NSE going up \n6. NSE going down  OR \n0 to exit: \n"))

    # Use the dictionary to execute the chosen case or exit
    case_function = switch.get(choice, lambda: print("Invalid choice"))
    case_function()
