# Exercise:
# Get 5 integers from a user, store them in a list, and print the maximum number.

# Initialize an empty list to store the integers
numbers = []

# Get 5 integers from the user
for i in range(5):
    num = int(input(f"Enter integer {i + 1}: "))
    numbers.append(num)

# Find the maximum number in the list
max_number = max(numbers)

# Print the maximum number
print(f"The maximum number is: {max_number}")
