def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) >= 2 and len(s) < 7 and s[:2].isalpha():
        switch = False
        for c in s[2:]:
            if switch == True and c.isalpha():
                return False
            elif switch == False and c == "0":
                return False
            elif c.isdigit():
                switch = True
            elif not c.isalnum():
                return False
        return True

    return False    



if __name__ == "__main__":
    main()