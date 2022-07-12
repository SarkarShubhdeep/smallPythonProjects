import random

print("Welcome to HighLow (Advanced)\n")
print("So who's gonna guess the number?"
      "\n1. ME - the human being"
      "\n2. COMPUTER - the machine")
choice = int(input("Enter your choice as 1 or 2: "))

# SETTINGS
max_lowest_val = 501
max_range_gap = 50


def guess_the_number(l, h):
    inp = int(input("Enter your number"))
    number_to_guess = random.randint(l, h)

    while inp != number_to_guess:
        if inp > h:
            print("Way too high. Guess lower.")
        elif inp < l:
            print("Way too low. Guess higher.")
        elif inp < number_to_guess:
            print("High.")
        elif inp > number_to_guess:
            print("Low.")
        else:
            return f"Yes! you got it. The number is {number_to_guess}"
        inp = int(input("Enter your number"))


def human_guess():
    lowest = random.randint(1, max_lowest_val)

    max_highest_val = lowest + max_range_gap

    highest = random.randint(lowest, max_highest_val)
    print(f"\nThink of a number between - {lowest} and {highest}")

    return guess_the_number(lowest, highest)


if choice == 1:
    # Input a range - highest and lowest
    # function - you guess highlow
    print(human_guess())
elif choice == 2:
    # Input a range - highest and lowest
    # function - computer guess highlow
    print()
else:
    print("Invalid choice. \n1. Try again?\n0. Quit")
    choice = input("Enter your choice as 1 or 2: ")
    if choice == 0:
        print("Thanks for playing. Bye.")
        # Here's the score
