import sys

def main():
    names = []
    while True:
        try:
            name = names.append(input("Name: "))
        except EOFError:
            print()
            break

    print("Adieu, adieu, to ", end="")
    if len(names) == 1:
        print(names[0])
    elif len(names) == 2:
        print(f"{names[0]} and {names[1]}")
    elif len(names) > 2:
        i = 0
        while i < len(names) - 1:
            print(f"{names[i]}, ", end="")
            i += 1
        print(f"and {names[i]}")


main()