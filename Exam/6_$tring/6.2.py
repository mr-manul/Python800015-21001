# Exercise:
# Write a program that gets a string from the user and prints the number of vowels in the string.

# Get a string from the user
user_string = input("Enter a string: ")

# Define a set of vowels
vowels = "aeiouAEIOU"

# Initialize a counter for vowels
vowel_count = 0

# Loop through each character in the string
for char in user_string:
    if char in vowels:
        vowel_count += 1

# Print the number of vowels
print(f"The number of vowels in the string is: {vowel_count}")
