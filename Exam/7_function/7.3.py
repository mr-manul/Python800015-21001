# Exercise:
# Define a function, convert_phonenumber(phone_num) which returns a modified string after removing ‘-’.
# Write a program that gets a phone number and prints it after removing ‘-’.

# Function to remove hyphens from the phone number
def convert_phonenumber(phone_num):
    return phone_num.replace("-", "")

# Get the phone number from the user
user_phone_num = input("Enter your phone number (format: 010-0000-0000): ")

# Convert the phone number by removing the hyphens
modified_phone_num = convert_phonenumber(user_phone_num)

# Print the modified phone number
print(f"Phone number without hyphens: {modified_phone_num}")
