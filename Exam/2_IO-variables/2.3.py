# Exercise:
# Get two integers from the user and output the remainder of division.
# Example:
# Input: 2, 4
# Output: The result is 2

# Get two integers from the user
num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))

# Perform division and calculate remainder
if num2 != 0:
    remainder = num1 % num2
    # Print the result
    print(f"The result is {remainder}")
else:
    print("Error: Division by zero is not allowed.")
