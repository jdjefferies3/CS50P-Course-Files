from pyfiglet import Figlet
import sys

def main():
    # Zero command line arguments
    if len(sys.argv) == 0:
        f = Figlet()
        print(f.rendterText(input("Input: ")))
    # Two command line arguments
    elif len(sys.argv) == 2:
        # Exit if not right amount of arguments
        if sys.argv[1] != "-f" or sys.argv[1] != "--font":
            sys.exit()
        else:
            f = Figlet(font=sys.argv[2])
            print(f.renderText(input("Input: ")))
    else:
        sys.exit()


main()