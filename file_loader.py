import pandas as pd
import os

# Define the directory containing CSV files
directory = 'D:/DU files/APT/focused/unraveled/unraveled APT/data/network-flows/Week1_Day1-2_05262021-05272021/cleaned'

# List all CSV files in the directory
csv_files = [file for file in os.listdir(directory) if file.endswith('.csv')]

# Initialize an empty dictionary to store DataFrames
dfs = {}

# Loop through each CSV file and read it into a DataFrame
for file in csv_files:
    file_path = os.path.join(directory, file)
    df_name = os.path.splitext(file)[0]  # Use file name (without extension) as DataFrame name
    dfs[df_name] = pd.read_csv(file_path)

# Access each DataFrame using its name (without extension)
for df_name, df in dfs.items():
    print(f"DataFrame '{df_name}':")
    print(df.head())  # Print the first few rows of each DataFrame
