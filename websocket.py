from kite_trade import KiteApp
import time
import pandas as pd
import winsound
from kiteconnect import KiteTicker
import re
import logging


# Read variables from 'variables.txt'
with open('variables.txt', 'r') as file:
    for line in file:
        exec(line)

# Initialize kite and retrieve user_id
enctoken = enc_token
kite = KiteApp(enctoken=enctoken)
user_id = kite.profile()["user_id"]
kws = KiteTicker(api_key="TradeViaPython", access_token=f"{enctoken}&user_id={user_id}")

# Define callback for tick reception
def on_ticks(ws, ticks):
    # Process received ticks
    for tick in ticks:
        if tick['instrument_token'] == your_instrument_token:
            ltp = tick['last_price']
            print("LTP for instrument {}: {}".format(tick['instrument_token'], ltp))

# Define callback for successful connection
def on_connect(ws, response):
    # Subscribe to the instrument's ticker
    ws.subscribe([your_instrument_token])

# Define callback for successful subscription
def on_subscribe(ws, response):
    pass

# Connect to WebSocket
kws.on_ticks = on_ticks
kws.on_connect = on_connect
kws.on_subscribe = on_subscribe
kws.connect()

# Run indefinitely
kws.connect(threaded=True)