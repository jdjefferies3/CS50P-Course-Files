# Create list to store items
item_list = []

while True:
    try:
        item_list.append(input("").lower())
    except EOFError:
        print()
        break

# Sort list
item_list.sort()

while len(item_list) > 0:

    item = item_list[0]
    print(f"{item_list.count(item)} {item.upper()}")
    while item in item_list:
        item_list.remove(item)