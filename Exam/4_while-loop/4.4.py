# Exercise:
# Get two positive integers and print their greatest common divisor (GCD).
# If a non-positive integer is entered, print an error message.

# Get two positive integers from the user
num1 = int(input("Enter the first positive integer: "))
num2 = int(input("Enter the second positive integer: "))

# Check if both numbers are positive
if num1 <= 0 or num2 <= 0:
    print("Error: Both numbers must be positive integers.")
else:
    # Use the Euclidean algorithm to find the GCD using a while loop
    while num2 != 0:
        num1, num2 = num2, num1 % num2

    # Print the GCD
    print(f"The greatest common divisor is: {num1}")
