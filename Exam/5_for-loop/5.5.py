import random

# Exercise:
# Calculate pi (π) using the Monte Carlo method

# Number of random points to generate (the higher, the more accurate)
num_points = 1000000

# Initialize counters
inside_circle = 0

# Generate random points and count how many fall inside the circle
for _ in range(num_points):
    # Randomly generate x and y between -1 and 1
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)

    # Check if the point (x, y) is inside the circle
    if x ** 2 + y ** 2 <= 1:
        inside_circle += 1

# Estimate the value of pi
pi_estimate = 4 * (inside_circle / num_points)

# Print the result
print(f"Estimated value of π using {num_points} points: {pi_estimate}")
