# Exercise:
# Calculate and print the sum of multiples of 3 between 1 and 100

total_sum = 0

# Loop through numbers from 1 to 100
for i in range(1, 101):
    if i % 3 == 0:
        total_sum += i

# Print the total sum
print(f"The sum of multiples of 3 between 1 and 100 is {total_sum}")


