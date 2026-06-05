import sys
import csv

def main():
    check_command_line()
    try:
        with open(sys.argv[1],"r") as before:
            reader = csv.DictReader(before)
            with open(sys.argv[2],"w") as after:
                writer = csv.DictWriter(after, fieldnames=["first","last","house"])
                writer.writeheader() # Writes column names using what's stored in fieldnames.
                for row in reader:
                    last, first = row["name"].split(",")
                    first = first.strip()
                    writer.writerow({"first": first, "last": last, "house": row["house"]})
    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")

def check_command_line():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

if __name__ == "__main__":
    main()
