# Exercise:
# Get 10 integers from the user and print their sum using a while loop.

# Initialize variables
count = 0
total_sum = 0

# Loop to get 10 integers
while count < 10:
    # Get an integer from the user
    num = int(input(f"Enter integer {count + 1}: "))

    # Add the number to the total sum
    total_sum += num

    # Increment the counter
    count += 1

# Print the total sum
print(f"The sum of the 10 integers is: {total_sum}")
