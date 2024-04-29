# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import data_cleaner


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    input_root_directory = 'D:/DU files/APT/focused/unraveled/unraveled APT/data/network-flows/Week6_Day6-7_07032021-07042021'
    output_root_directory = 'D:/DU files/APT/focused/unraveled/unraveled APT/data/network-flows/Week6_Day6-7_07032021-07042021/cleaned'
    data_cleaner.clean_csv_files_in_directory(input_root_directory, output_root_directory,89)

    print("All CSV files cleaned successfully and saved to the output directory.")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
