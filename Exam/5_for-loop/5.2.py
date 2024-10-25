import random

# Exercise:
# Simulate rolling a dice 100 times and count the number of occurrences of 6

occurrences_of_six = 0

# Simulate rolling a dice 100 times
for _ in range(100):
    roll = random.randint(1, 6)  # Simulates a dice roll (1 to 6)
    if roll == 6:
        occurrences_of_six += 1

# Print the number of times 6 occurred
print(f"The number 6 appeared {occurrences_of_six} times when rolling the dice 100 times.")
