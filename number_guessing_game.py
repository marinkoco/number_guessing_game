import random
import time

def guess_number():
    secret_number = random.randint(1, 100)
    attempts = 10

    print("Welcome to the Number Guessing Game!")
    print("I am thinking of a number between 1 and 100.")

    while True:
        print("You have", attempts, "attempts.")
        guess = input("Take a guess: ")
        if guess.isdigit() and 1 <= int(guess) <= 100:
            guess = int(guess)
            attempts -= 1
        else:
            print("Wrong input. Please input a number between 1 and 100.")
            continue

        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print("Congratulations! You guessed the number in", attempts, "attempts.")
            time.sleep(5)
            break

        if attempts == 0:
            print("Sorry, you've reached the maximum number of attempts.")
            print("The secret number was:", secret_number)
            time.sleep(5)
            break

guess_number()
