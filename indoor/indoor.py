# Implement a program in Python that prompts the user for input and then outputs that same input in lowercase.
# Punctuation and whitespace should be outputted unchanged

def main():
    # Request input string from user
    temp = input("Enter string: ")

    # Call function to lowercase input string
    print(lower(temp))

def lower(inputStr):
    # Return input string in lowercase
    return inputStr.lower()

main()