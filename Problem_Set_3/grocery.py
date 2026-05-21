total_items = []
total_types = set()

while True:
    try:
        item = input().upper()
        total_items.append(item)
        total_types.add(item)
    except EOFError:
        break

items = sorted(list(total_types)) # sorted() to rearrange list into alphabetical order

for i in range(len(items)):
    n = total_items.count(items[i])
    print(f"{n} {items[i]}")