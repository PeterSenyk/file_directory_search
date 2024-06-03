"""
Program to find files in a file directory tree and return file paths
@author: Peter Senyk
@version: 2024_0.2
"""

import csv
from datetime import datetime


def find_file_in_tree(file_path, filename):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    file_path_dictionary = check_lines(lines[::-1], filename)
    return file_path_dictionary


def check_lines(lines, filename):
    file_path_dictionary = {}
    count = 0
    for line in lines:
        if filename in line:
            count += 1
        elif "Directory" in line and count > 0:
            dir_line = clean_directory_line(line)
            file_path_dictionary[dir_line] = count
            count = 0
    return file_path_dictionary


def clean_directory_line(line):
    dir_line = line.lstrip(" ").strip("Directory: ")
    return dir_line


def clean_dictionary_results(file_path_dictionary):
    for key, value in file_path_dictionary.items():
        print(f"{key}\nContains {value} files containing the search\n")


def export_file_paths(path_dictionary, output_path):
    current_date = datetime.now().strftime("%y-%m-%d")
    file_name = f"Filepath_Output_{current_date}.csv"
    file_output = output_path + "\\" + file_name

    with open(file_output, "w", newline="") as output_file:
        writer = csv.writer(output_file)
        writer.writerow(["File Path", "Number of Files"])

        for path, number in path_dictionary.items():
            writer.writerow([path, number])


if __name__ == '__main__':
    tree_file_path = r"D:\testScripts\powershell_tree.txt"  # Path to the tree file
    output_file_path = r"D:\testScripts\testOutput"  # Output file path
    search_filename = input("Enter your search: ")  # Filename to search for

    file_paths = find_file_in_tree(tree_file_path, search_filename)
    export_file_paths(file_paths, output_file_path)
