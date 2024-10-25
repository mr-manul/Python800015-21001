# Exercise:
# Get an integer and print all its divisors using a while loop.
# If 0 or a negative number is entered, print an error message.

# Get an integer from the user
num = int(input("Enter a positive integer: "))

# Check if the number is positive
if num <= 0:
    print("Error: Please enter a positive integer.")
else:
    print(f"Divisors of {num} are:")

    # Initialize a counter
    i = 1

    # Loop to find and print all divisors
    while i <= num:
        if num % i == 0:
            print(i)
        i += 1
