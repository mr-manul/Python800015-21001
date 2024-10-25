# Exercise:
# Define a function, check_valid_phone(phone_num) which returns True/False if the phone number is valid.
# Write a program that gets a phone number and prints whether it is valid or not.

# Function to check if a phone number is valid
def check_valid_phone(phone_num):
    # Remove any hyphens from the phone number
    cleaned_phone_num = phone_num.replace("-", "")

    # Check if the phone number has exactly 11 digits and is numeric
    if len(cleaned_phone_num) == 11 and cleaned_phone_num.isdigit():
        return True
    else:
        return False


# Get the phone number from the user
user_phone_num = input("Enter your phone number (e.g., 010-1234-5678): ")

# Check if the phone number is valid
if check_valid_phone(user_phone_num):
    print("The phone number is valid.")
else:
    print("The phone number is not valid.")
