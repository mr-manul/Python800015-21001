import random

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)

# Initialize the user's guess
guess = None

# Start the guessing loop
while guess != secret_number:
    # Get the user's guess
    guess = int(input("Guess the number (between 1 and 100): "))

    # Check if the guess is higher, lower, or correct
    if guess < secret_number:
        print("Higher!")
    elif guess > secret_number:
        print("Lower!")
    else:
        print("Congratulations! You guessed the right number.")
