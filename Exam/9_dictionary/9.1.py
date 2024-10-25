# Exercise:
# 1. Store 5 entries (name and phone number) from the user.
# 2. After storing, get a name to search from the user and print the corresponding phone number.
# 3. If the name is not found, print a message.

# Initialize an empty dictionary to store name and phone number entries
phonebook = {}

# Store 5 entries in the phonebook
for i in range(5):
    name = input(f"Enter name {i + 1}: ")
    phone_number = input(f"Enter {name}'s phone number: ")
    phonebook[name] = phone_number

# Get the name to search from the user
search_name = input("\nEnter the name to search for: ")

# Search for the name in the phonebook
if search_name in phonebook:
    print(f"{search_name}'s phone number is {phonebook[search_name]}")
else:
    print(f"Error: {search_name} not found in the phonebook.")

