def main():
    prompt = get_fuel("Fraction: ")

    print(prompt)

def get_fuel(s):
    while True:
        # Separate given string into 2 sides with '/'
        fraction = input(s).split("/")
        try:
            x = int(fraction[0])
            y = int(fraction[1])
            if x > y:
                continue
            div = round(x/y * 100)
            if div <= 1:
                return "E"
            elif div >= 99:
                return "F"
            return str(div) + "%"
        except ValueError:
            pass
        except ZeroDivisionError:
            pass



main()