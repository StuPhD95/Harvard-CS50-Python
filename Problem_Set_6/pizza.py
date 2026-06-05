import sys
import csv
from tabulate import tabulate # Only function in tabulate module.

def main():
    check_command_line()
    check_extension()
    try:
        with open(sys.argv[1],"r") as file:
            reader = csv.reader(file)
            print(tabulate(reader, headers="firstrow", tablefmt="grid"))
    except FileNotFoundError:
        sys.exit("File does not exist")

def check_command_line():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

def check_extension():
    if not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV file")

if __name__ == "__main__":
    main()