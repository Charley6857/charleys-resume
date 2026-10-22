
import random

print("Welcome to my Number Guessing Game!")

# Generate a random number between 1 and 10
secret_number = random.randint(1, 10)

# Set the starting guess
guess = 0

# Keep asking until the player guesses correctly
while guess != secret_number:

    # Ask the player to enter a number
    guess = int(input("Guess a number between 1 and 10: "))

    # Check whether the guess is correct
    if guess == secret_number:
        print("Congratulations! You guessed correctly!")

    # If the guess is incorrect, try again
    else:
        print("Sorry! Try again!")

print("Thanks for playing my game!")
