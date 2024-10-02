#input
A = input("Enter First String: ")
B = input("Enter Second String: ")

indexes = []

start = 0

while True:
    start = A.find(B, start)
    if start == -1:
        break
    indexes.append(start)
    start += 1

#output
if indexes:
    print("Indexes:", ' '.join(map(str, indexes)))
else:
    print(-1)