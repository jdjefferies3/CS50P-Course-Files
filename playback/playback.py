# Implement a program in Python that prompts the user for input and then outputs that same input, replacing each space with ... (i.e., three periods)

def main():
    # Prompt user for input and save string
    temp = input("Enter string: ")

    print(temp.replace(" ", "..."))

main()