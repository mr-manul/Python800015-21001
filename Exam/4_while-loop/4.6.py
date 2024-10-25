# Exercise:
# Write a program that gets a positive integer and calculates its square root using an approximation.
# Do not use library functions or the exponent operator (**).

# Get the positive integer from the user
num = int(input("Enter a positive integer: "))

# Check if the number is positive
if num <= 0:
    print("Error: Please enter a positive integer.")
else:
    # Initial guess for the square root (starting at num / 2)
    guess = num / 2.0
    # Define the tolerance for the approximation
    tolerance = 0.00001

    # Use the Babylonian method (Newton-Raphson method) to approximate the square root
    while abs(guess * guess - num) > tolerance:
        guess = (guess + num / guess) / 2.0

    # Print the approximated square root
    print(f"The approximate square root of {num} is {guess:.5f}")
