import random
import sys

def main():


    level = get_level()

    rand = random.randint(0, level)

    while True:
        try:
            guess = int(input("Guess: "))
            if guess < 0:
                raise ValueError("Invalid number")
            else:
                if guess < rand:
                    print("Too small!")
                    pass
                elif guess > rand:
                    print("Too large!")
                    pass
                else:
                    print("Just right!")
                    sys.exit(1)
        except ValueError:
            pass



def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level < 0:
                raise ValueError()
            return level
        except ValueError:
            pass

main()