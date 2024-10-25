# Exercise:
# Get two integers from the user and output the result of division.
# Example:
# Input: 2, 4
# Output: The result is 0.5

# Get two integers from the user
num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))

# Perform division
if num2 != 0:
    result = num1 / num2
    # Print the result
    print(f"The result is {result}")
else:
    print("Error: Division by zero is not allowed.")
