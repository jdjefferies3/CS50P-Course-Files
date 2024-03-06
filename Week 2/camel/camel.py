def main():
    # Ask user for input of camelCase
    camel = input("camelCase: ")
    # Print snake case
    print(snake_case(camel))

def snake_case(string):
    snake = ""
    # Parse string
    for c in string:
        # If c is not capital add to string
        if not c.isupper():
            snake += c
        else:
            snake += "_" + c.lower()
    
    return snake

main()