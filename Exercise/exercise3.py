import re

# Function to validate the phone number format
def is_valid_phone_number(phone_number):
    pattern = r"^\d{3}-\d{4}-\d{4}$"
    return re.match(pattern, phone_number)

# Get input from the user
phone_number = input("Enter mobile phone number (format: xxx-xxxx-xxxx): ")

cleaned_number = phone_number.replace("-", "")

if is_valid_phone_number(phone_number):
    # Remove dashes from the phone number
    cleaned_number = phone_number.replace("-", "")
    print("Cleaned Phone Number:", cleaned_number)
else:
    print("Invalid format. Please use the format xxx-xxxx-xxxx.")