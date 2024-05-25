import re

def extract_stock_symbol(line):
    # Extract stock symbol from the line
    match = re.search(r'[A-Za-z]+', line)
    return match.group(0).strip().lower() if match else None

def display_non_duplicates(file_path):
    # Use a set to track seen cleaned stock symbols
    seen_symbols = set()

    # Display non-duplicate stock symbols
    print("Non-Duplicate Stocks:")
    with open(file_path, 'r') as file:
        for line in file:
            symbol = extract_stock_symbol(line)
            if symbol and symbol not in seen_symbols:
                seen_symbols.add(symbol)
                print(symbol)

# Replace 'your_file.txt' with the actual path to your input file
#display_non_duplicates('your_file.txt')


display_non_duplicates('todays_stock.txt')
