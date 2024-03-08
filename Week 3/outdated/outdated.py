months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

def main():
    while True:
        try:
            input_date = input("Date: ")
            print(switch_date(input_date))
            break
        except EOFError:
            print()
            break


def switch_date(in_date):
    # If date is in MM/dd/YYYY
    if in_date[:1].isdigit():
        sep = in_date.split("/")
        return f"{sep[2]}-{sep[0].zfill(2)}-{sep[1].zfill(2)}"

    # If date is in Month day, YEAR
    elif in_date[:1].isalpha():
        sep = in_date.split(" ")
        day = sep[1].replace(",", "").zfill(2)
        return f"{sep[2]}-{str(months.index(sep[0]) + 1).zfill(2)}-{day}"


main()
