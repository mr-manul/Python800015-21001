# Exercise:
# Write a program that gets a mobile phone number in the form of 010-0000-0000
# and prints it by removing the hyphens (-), such as 0100000000.

# Get the mobile phone number from the user
phone_number = input("Enter your phone number (format: 010-0000-0000): ")

# Remove hyphens from the phone number
cleaned_phone_number = phone_number.replace("-", "")

# Print the phone number without hyphens
print(f"Phone number without hyphens: {cleaned_phone_number}")
