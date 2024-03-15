import random

def main():
    level = get_level()
    num_correct = 0

    for i in range(10):
        # Generate equation
        x = generate_integer(level)
        y = generate_integer(level)
        solution = x + y
        num_wrong = 0
        while num_wrong != 3:
            user_solution = int(input(f"{x} + {y} = "))
            if user_solution == solution:
                num_correct += 1
                break
            else:
                print("EEE")
                num_wrong += 1
        print(f"{x} + {y} = {solution}")
        
    
    print(f"Score: {num_correct}")
    

def get_level():
    # Prompt user for level
    # Only accept 1, 2, or 3
    while True:
        try:
            inp = int(input("Level: "))
            if inp == 1 or inp == 2 or inp == 3:
                return int(inp)
            else:
                raise ValueError
        except ValueError:
            pass
        except TypeError:
            pass

def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)

if __name__ == "__main__":
    main()