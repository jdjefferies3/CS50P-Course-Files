import sys
from tabulate import tabulate

def main():
    if len(sys.argv) < 2:
        print("Too few command-line arguments")
        sys.exit(1)
    elif len(sys.argv) > 2:
        print("Too many command-line arguments")
        sys.exit(1)
    else:
        table = []
        try:
            split = sys.argv[1].split(".")
            if len(split) == 1 or (len(split) > 1 and split[1] != "csv"):
                print("Not a CSV file")
                sys.exit(1)
            with open(sys.argv[1]) as file:
                for line in file:
                    pizza_name, type_one, type_two = line.rstrip().split(",")
                    table.append([pizza_name, type_one, type_two])
                    # print(f"Pizza Name: {pizza_name}, Type 1: {type_one}, Type 2: {type_two}")
                
                type = table[0][0]
                price_small = table[0][1]
                price_large = table[0][2]
                table.pop(0)
                print(tabulate(table, headers=[type, price_small, price_large], tablefmt="grid"))

        except ValueError:
            sys.exit()
        except FileNotFoundError:
            print("File does not exist")
            sys.exit(1)


if __name__ == "__main__":
    main()