import argparse
import os

def parse_arguments():
    parser = argparse.ArgumentParser(description='View directory structure.')
    parser.add_argument('directory', type=str, help='The directory to view')
    args = parser.parse_args()
    return args

def print_directory(directory):
    for item in os.listdir(directory):
        print(item)

if __name__ == "__main__":
    args = parse_arguments()
    print_directory(args.directory)
