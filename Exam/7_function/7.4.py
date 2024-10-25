# Exercise:
# Define a function, convert_string(phone_num, remove_target) which returns a modified string after removing all letters that belong to remove_target.
# Write a program that gets a phone number and prints it after removing specified characters.

# Function to remove all characters in remove_target from phone_num
def convert_string(phone_num, remove_target):
    modified_string = ""
    for char in phone_num:
        if char not in remove_target:
            modified_string += char
    return modified_string

# Get the phone number from the user
user_phone_num = input("Enter your phone number: ")

# Get the characters to remove from the user
remove_target = input("Enter the characters to remove (e.g. '-'): ")

# Convert the phone number by removing the specified characters
modified_phone_num = convert_string(user_phone_num, remove_target)

# Print the modified phone number
print(f"Phone number after removing '{remove_target}': {modified_phone_num}")

