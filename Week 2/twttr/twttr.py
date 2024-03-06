def main():
    # Get string from user
    str = input("Input: ")
    # Print vowelless string
    print(remove_vow(str))

def remove_vow(s):
    ret = ""
    # Iterate through string
    for c in s:
        temp = c.lower()
        # Check if character is a vowel
        match temp:
            case "a" | "e" | "i" | "o" | "u":
                continue
            case _:
                ret += c
    
    return ret

main()