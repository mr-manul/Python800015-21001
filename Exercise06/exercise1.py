input = int(input("Please enter a number: "))

even = []

for i in range(1, input, 1):
    if i % 2 == 0:
        even.append(i)

print(even)
