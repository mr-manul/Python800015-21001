# Exercise:
# Get 10 real numbers from the user and print the greatest one

# Initialize the greatest number to negative infinity
greatest = float('-inf')

# Loop to get 10 real numbers
for i in range(10):
    num = float(input(f"Enter real number {i + 1}: "))

    # Update the greatest number if the current number is greater
    if num > greatest:
        greatest = num

# Print the greatest number
print(f"The greatest number is: {greatest}")
