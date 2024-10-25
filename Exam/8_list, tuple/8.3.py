# Exercise:
# Get 5 integers from a user, store them in a list, and print the list sorted in descending order without using reverse().

# Initialize an empty list to store the integers
numbers = []

# Get 5 integers from the user
for i in range(5):
    num = int(input(f"Enter integer {i + 1}: "))
    numbers.append(num)

# Sort the list in descending order
sorted_numbers = sorted(numbers, reverse=True)

# Print the sorted list in descending order
print(f"The list sorted in descending order: {sorted_numbers}")

