# Exercise:
# Create a phonebook program where the user can input, search, delete entries, or quit the program.

# Initialize an empty dictionary to store name and phone number entries
phonebook = {}

while True:
    # Prompt the user for a command
    command = input("Type the command (input, search, delete, or quit): ").lower()

    if command == "input":
        # Input a new name and phone number
        name = input("Enter name: ")
        phone_number = input("Enter phone number: ")
        phonebook[name] = phone_number
        print(f"{name}'s phone number has been successfully added.")

    elif command == "search":
        # Search for a name and print the associated phone number
        search_name = input("Enter the name to search: ")
        if search_name in phonebook:
            print(f"{search_name}'s phone number is {phonebook[search_name]}")
        else:
            print(f"Error: {search_name} not found in the phonebook.")

    elif command == "delete":
        # Delete an entry by name
        delete_name = input("Enter the name to delete: ")
        if delete_name in phonebook:
            del phonebook[delete_name]
            print(f"{delete_name} has been successfully deleted.")
        else:
            print(f"Error: {delete_name} not found in the phonebook.")

    elif command == "quit":
        # Exit the program
        print("Exiting program...")
        break

    else:
        print("Invalid command, please try again.")
