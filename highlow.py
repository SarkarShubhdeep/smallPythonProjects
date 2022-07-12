import random


def guess_the_number(x):
    n = random.randint(1, x)

    user_inp = int(input(f"Ok, enter a number between 1 and {x}: "))
    i = 0

    while user_inp != n:
        if user_inp > x:
            user_inp = int(input(f"What did I say, BETWEEN 1 AND {x}. LOWER!!: "))
        elif user_inp > n:
            user_inp = int(input("Guess lower: "))
        elif user_inp < n:
            user_inp = int(input("Guess higher: "))
        i += 1
        if i == 5:
            print("So, you're new to this game. Take your time buddy. 😒")
        if i == 10:
            return f"Forget it. The number was {n}. How hard could it be? 😪"

    return f"Yes! you got it. The number was {n}"


print(guess_the_number(50))

