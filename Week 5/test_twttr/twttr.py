def main():
    # Get string from user
    str = input("Input: ")
    # Print vowelless string
    print(shorten(str))

def shorten(word):
    if word.isdigit():
        return ""
    ret = ""
    # Iterate through string
    for c in word:
        temp = c.lower()
        # Check if character is a vowel
        match temp:
            case "a" | "e" | "i" | "o" | "u":
                continue
            case _:
                ret += c
    
    return ret

if __name__ == "__main__":
    main()