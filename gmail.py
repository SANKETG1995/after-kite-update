import pandas as pd

# Replace 'your_file.csv' with the actual name of your CSV file
csv_file = 'SheetData.csv'

# Read the CSV file into a pandas DataFrame
df = pd.read_csv(csv_file)

# Display the contents of the DataFrame
print("CSV File Contents:")
print(df)