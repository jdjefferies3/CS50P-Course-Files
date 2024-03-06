def main():
    amount_left = 50
    while amount_left > 0:
        print(f"Amount Due: {amount_left}")
        entered = int(input("Insert Coin: "))
        # Check if number is 25, 10, or 5
        match entered:
            case 25 | 10 | 5:
                amount_left -= entered
            case _:
                continue
    print("Change Owed:", abs(amount_left))


main()