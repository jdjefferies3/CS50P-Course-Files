import sys

def main():
    if len(sys.argv) == 1:
        print("Too few command-line arguments")
        sys.exit
    elif len(sys.argv) == 2:
        # Check if file ends in '.py'
        try:
            split = sys.argv[1].split(".")
            if len(split) == 1 or (len(split) > 1 and split[1] != "py"):
                print("Not a python file")
                sys.exit()
            with open(sys.argv[1]) as file:
                count = 0
                for line in file:
                    if not line.strip() or line.strip().startswith("#"):
                        pass
                    else:
                        count += 1
                print(count)
        except ValueError:
            sys.exit()
        except FileNotFoundError:
            print("File does not exist")
            sys.exit()
    elif len(sys.argv) > 2:
        print("Too many command-line arguments")
        sys.exit()

if __name__ == "__main__":
    main()