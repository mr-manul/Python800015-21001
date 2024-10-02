A = input("Enter String: ")

vowels = "aeiou"

count = 0

for char in A:
    if char in vowels:
        count += 1

print("Number of vowels:", count)
