# Ask user for their name, remove whitespace and capitalize
# name = input("What's your name? ").strip().title()

# Say hello to user
# print(f"hello, {name}")

def main():
    name = input("What's your name? ")
    hello(name)

def hello(to="world"):
    print(f"hello, {to}")

main()