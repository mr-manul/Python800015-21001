import random

simulated = 100000
count = 0

for i in range(simulated):
    rolls = [random.randint(1, 6) for i in range(10)]

    if any(rolls.count(number) == 5 for number in set(rolls)):
        count += 1

probability = count / simulated
print("Probability same number:", probability)


