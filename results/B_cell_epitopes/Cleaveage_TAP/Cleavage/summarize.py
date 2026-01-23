import pandas as pd

# Load the csv file to inspect the contents
csv_file = '/mnt/data/result.csv'
data = pd.read_csv(csv_file)

# Display the first few rows of the data
data.head()

