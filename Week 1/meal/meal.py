def main():
    in_time = input("What time is sit? ")
    con = convert(in_time)

    if 7 <= con <= 8:
        print("breakfast time")
    elif 12 <= con <= 13:
        print("lunch time")
    elif 18 <= con <= 19:
        print("dinner time")



def convert(time):
    str_split = time.split(":", -1)
    hours = str_split[0]
    # print(hours)
    mins = str_split[1]
    # print(mins)
    time_float = float(hours) + float(mins) / 60.0
    # print(time_float)
    return time_float


if __name__ == "__main__":
    main()