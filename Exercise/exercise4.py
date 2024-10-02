#input
A = input("Enter String: ")

char_array = list(A)

counts = []

result = ""
count = 1

# Iterate through the string
for i in range(len(A)):
    # Check if the next character is the same as the current one
    if i < len(A) - 1 and A[i] == A[i + 1]:
        count += 1
    else:
        # Append the character and its count to the result string
        result += A[i] + str(count)
        count = 1  # Reset count for the next character

# Print the resulting string
print("Output:", result)