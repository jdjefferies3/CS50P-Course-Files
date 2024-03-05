def main():
    # Prompt the user for input to convert
    temp = input("Please enter an emoticon: ")

    # Call convert() on the input string
    print(convert(temp))


def convert(tempString):
    # Replace ':)' and ':(' in string
    tempString = tempString.replace(":)", "\N{slightly smiling face}")
    tempString = tempString.replace(":(", "\N{slightly frowning face}")

    return tempString

main()