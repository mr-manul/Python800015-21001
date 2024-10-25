import random

# Exercise:
# Calculate pi (π) using the Monte Carlo method, generating random points between 0 and 1

# Number of random points to generate (the higher, the more accurate)
num_points = 1000000

# Initialize counters
inside_circle = 0

# Generate random points and count how many fall inside the circle
for _ in range(num_points):
    # Generate random x and y coordinates between 0 and 1
    x = random.random()  # random() generates a number between 0 and 1
    y = random.random()

    # Check if the point (x, y) is inside the quarter circle
    if x ** 2 + y ** 2 <= 1:
        inside_circle += 1

# Estimate the value of pi using the ratio of points inside the circle
# Since we're working with a quarter circle, we multiply by 4 to get pi
pi_estimate = 4 * (inside_circle / num_points)

# Print the result
print(f"Estimated value of π using {num_points} points: {pi_estimate}")
