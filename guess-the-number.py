import random

def guess(x):
    random_numb = random.randint(1, x)
    guess = 0
    while guess != random_numb:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        if guess < random_numb:
            print("You guessed wrong, HAHA! Maybe you're too low...")
        elif guess > random_numb:
            print("You guessed wrong, HAHA! Maybe you're too high...")

    print(f"Ok, it seems you guessed the number {random_numb} right... You won this time.")

guess(10)
