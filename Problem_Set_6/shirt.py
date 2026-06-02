import sys
from PIL import Image, ImageOps # Import multiple functions from the same module.

def main():
    check_command_line_length()
    check_file_extensions()
    try:
        with Image.open(sys.argv[1]) as before:
            cs50_shirt = Image.open("shirt.png")
            size = cs50_shirt.size # Returns a tuple.
            before = ImageOps.fit(before, size)
            before.paste(cs50_shirt,cs50_shirt)
            before.save(sys.argv[2])
    except FileNotFoundError:
        sys.exit("Input does not exist")

def check_command_line_length():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

def check_file_extensions():
    extensions = (".jpg", ".jpeg",".png")
    """ endswith()
    - Returns a Boolean.
    - Argument can be a single string, or a tuple of strings, but NOT a list of strings.
    """
    if not sys.argv[1].lower().endswith(extensions):
        sys.exit("Invalid input")
    elif not sys.argv[2].lower().endswith(extensions):
        sys.exit("Invalid output")
    for i in range(len(extensions)):
        if sys.argv[1].lower().endswith(extensions[i]) != sys.argv[2].lower().endswith(extensions[i]):
            sys.exit("Input and output have different extensions")

if __name__ == "__main__":
    main()