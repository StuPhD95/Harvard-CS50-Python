import sys

if len(sys.argv) == 1:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif sys.argv[1].endswith(".py") != True:
    sys.exit("Not a Python file")
else:
    try:
        with open(sys.argv[1]) as file: # Default option for open is "r".
            line_count = 0
            for line in file:
                if line.lstrip().startswith("#"): # lstrip() runs first then startswith()
                    pass
                elif line.isspace():
                    pass
                else:
                    line_count += 1
            print(line_count)
    except FileNotFoundError:
        sys.exit("File does not exist")
