import os
import re
import pandas as pd
from pprint import pprint
import io


# Define data cleaning function
# Function to count fields in a CSV row
def count_fields(line, delimiter=','):
    return len(line.split(delimiter))

def clean_data(df):
    # Example: Remove leading and trailing whitespaces from all columns
    df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)
    # Example: Drop rows with missing values
    df.dropna(inplace=True)
    return df


# Function to clean CSV files in a directory
def clean_csv_files_in_directory(input_directory, output_directory, expected_field_count):
    for root, dirs, files in os.walk(input_directory):
        for file in files:
            if file.endswith('.csv'):
                input_file_path = os.path.join(root, file)
                output_file_path = os.path.join(output_directory, os.path.relpath(input_file_path, input_directory))
                output_file_dir = os.path.dirname(output_file_path)
                os.makedirs(output_file_dir, exist_ok=True)
                print("Processing:", input_file_path)

                cleaned_lines = []
                with open(input_file_path, 'r', encoding='utf-8') as infile:
                    for line in infile:
                        field_count = count_fields(line)
                        if field_count == expected_field_count:
                            cleaned_lines.append(line)
                        else:
                            print(f"Skipped {line} due to field mismatch: {field_count} expected: {expected_field_count}")

                # Write cleaned lines to a new CSV file
                with open(output_file_path, 'w', encoding='utf-8') as outfile:
                    outfile.writelines(cleaned_lines)

                # Read the cleaned CSV file into a DataFrame and apply additional cleaning
                # df = pd.read_csv(output_file_path, delimiter=',')
                # df_cleaned = clean_data(df)
                # df_cleaned.to_csv(output_file_path, index=False)  # Save cleaned DataFrame back to CSV

                print("Cleaning completed. Saved to:", output_file_path)