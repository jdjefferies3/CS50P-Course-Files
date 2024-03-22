def main():
    while True:
        prompt = input("Fraction: ")
        try:
            frac = convert(prompt)
            if isinstance(frac, int):
                print(gauge(frac))
                break

        except ValueError:
            pass
        except ZeroDivisionError:
            pass
        
        
def convert(fraction):
    pieces = fraction.split("/")
    x = pieces[0]
    y = pieces[1]
    if x.isalpha() == True or y.isalpha() == True:
        raise ValueError
    x = int(x)
    y = int(y)
    if y == 0:
        raise ZeroDivisionError
    elif x > y:
        raise ValueError
    return round(x/y * 100)


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    return str(percentage) + "%"
    



if __name__ == "__main__":
    main()