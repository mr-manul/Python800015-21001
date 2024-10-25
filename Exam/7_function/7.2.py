# Exercise:
# Define a function, sum_range(num1, num2) which returns the sum from num1 to num2.
# By calling sum_range(), print the sum from 100 to 200.

# Function to calculate the sum of all integers from num1 to num2
def sum_range(num1, num2):
    total = 0
    for i in range(num1, num2 + 1):
        total += i
    return total

# Call the function to calculate the sum from 100 to 200
result = sum_range(100, 200)

# Print the result
print(f"The sum from 100 to 200 is: {result}")
