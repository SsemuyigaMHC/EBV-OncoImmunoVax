import pandas as pd

# Correct path to the CSV file from the WSL directory
csv_file = '/mnt/c/Users/MHC V(D)J/EBV/TAP/result.csv'

# Try reading the CSV file
data = pd.read_csv(csv_file)

# Display the first few rows to verify
print(data.head())

