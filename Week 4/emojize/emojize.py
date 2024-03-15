import emoji

def main():
    inp = input("Input: ")
    print(emoji.emojize("Output: " + inp, language="alias"))


main()
