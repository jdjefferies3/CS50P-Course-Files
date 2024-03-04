def main():
    # Prompt user to input mass
    mass = input("Please enter mass: ")

    # Print return from energy()
    print(energy(mass))

def energy(num):
    # Calculate E for E=mc^2
    e = int(num) * (300000000 ** 2)
    return e

main()