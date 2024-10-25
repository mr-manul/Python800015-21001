# Exercise:
# Get an integer from the user and output whether it is "positive", "negative", or "zero".
# Example:
# Input: 5
# Output: positive

# Get an integer from the user
num = int(input("Enter an integer: "))

# Check if the number is positive, negative, or zero
if num > 0:
    print("positive")
elif num < 0:
    print("negative")
else:
    print("zero")
