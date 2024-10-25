import random

# Exercise:
# Simulate rolling two dice and calculate the probability that both dice show the same number

# Number of simulations (higher number for better approximation)
num_trials = 100000

same_count = 0

# Simulate rolling two dice num_trials times
for _ in range(num_trials):
    die1 = random.randint(1, 6)  # Roll the first die
    die2 = random.randint(1, 6)  # Roll the second die

    if die1 == die2:
        same_count += 1  # Count if both dice show the same number

# Calculate the probability
probability = same_count / num_trials

# Print the approximated probability
print(f"Approximate probability that both dice show the same number: {probability:.4f}")
