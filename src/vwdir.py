"""
This module provides functions to view the directory structure.

It defines the following functions:
- parse_arguments: Parses command line arguments and returns the parsed arguments.
- print_directory: Prints the contents of a directory.

"""
# src/vwdir.py

import argparse
import os

def parse_arguments():
    """
    Parse command line arguments and return the parsed arguments.

    This function uses the `argparse` module to parse command line arguments.
    It defines a single argument `directory` of type `str` which specifies the directory to view.
    The function returns the parsed arguments as an `argparse.Namespace` object.

    Returns:
        argparse.Namespace: The parsed command line arguments.

    """

    parser = argparse.ArgumentParser(description='View directory structure.')
    parser.add_argument('directory', type=str, help='The directory to view')
    parsed_args = parser.parse_args()

    return parsed_args

def print_directory(directory):
    """
    Print the contents of a directory.

    Args:
        directory (str): The path to the directory.

    Returns:
        None
    """

    for item in sorted(os.listdir(directory)):
        print(item)

if __name__ == "__main__":
    args = parse_arguments()
    print_directory(args.directory)
