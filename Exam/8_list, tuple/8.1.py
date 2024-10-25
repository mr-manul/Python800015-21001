# Exercise:
# Get a positive integer from a user and store all even numbers less than the integer in a list.
# Print the list of even numbers.

# Get a positive integer from the user
num = int(input("Enter a positive integer: "))

# Initialize an empty list to store even numbers
even_numbers = []

# Loop through all numbers less than the entered integer
for i in range(1, num):
    if i % 2 == 0:  # Check if the number is even
        even_numbers.append(i)

# Print the list of even numbers
print(even_numbers)
