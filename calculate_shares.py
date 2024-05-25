import sys

# Retrieve the user variable from command-line arguments
if len(sys.argv) != 2:
    print("Usage: python second_script.py <user_variable>")
    sys.exit(1)
     
def calculate_number_of_shares(trading_capital, leverage, stock_price):
    """
    Calculate the number of shares that can be bought in intraday trading.

    Parameters:
    - trading_capital (float): The amount of capital available for trading.
    - leverage (float): The leverage provided by the broker.
    - stock_price (float): The current price of the stock.

    Returns:
    - float: The number of shares that can be bought.
    """
    number_of_shares = (trading_capital * leverage) / stock_price
    return number_of_shares

# Example usage:
trading_capital = 8729 # Replace with your trading capital
leverage = 5  # Replace with the leverage provided by your broker
stock_price =  float(sys.argv[1]) # Replace with the current price of the stock

shares_to_buy = calculate_number_of_shares(trading_capital, leverage, stock_price)
print(f"You can buy {int(shares_to_buy)} shares with {trading_capital} capital.")
#######

#CQ9fFuf3 ns7LFnzP kPc7RFOG rcKmp28z blU1qWja Ip4KdxIT
##
##