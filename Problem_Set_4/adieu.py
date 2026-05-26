import inflect

names = []

while True:
    try:
        name = input("Name: ")
        names.append(name)
    except EOFError:
        print() # Python doesn't automatically move to a new line after terminating input (e.g. ctrl + d).
        break

p = inflect.engine() # Automatic grammar formatting.

print("Adieu, adieu, to " + p.join(names))