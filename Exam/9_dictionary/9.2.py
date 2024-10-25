# Exercise:
# Create a menu-based phonebook program with options to input, search, delete, and quit.

# Initialize an empty dictionary to store name and phone number entries
phonebook = {}

while True:
    # Display menu options
    print("\nMenu: ")
    print("1. input")
    print("2. search")
    print("3. delete")
    print("4. quit")

    # Get the user's choice
    choice = input("Enter your choice: ").lower()

    if choice == "input":
        # Input a new name and phone number
        name = input("Enter name: ")
        phone_number = input("Enter phone number: ")
        phonebook[name] = phone_number
        print(f"{name}'s phone number has been successfully added.")

    elif choice == "search":
        # Search for a name and print the associated phone number
        search_name = input("Enter the name to search: ")
        if search_name in phonebook:
            print(f"{search_name}'s phone number is {phonebook[search_name]}")
        else:
            print(f"Error: {search_name} not found in the phonebook.")

    elif choice == "delete":
        # Delete an entry by name
        delete_name = input("Enter the name to delete: ")
        if delete_name in phonebook:
            del phonebook[delete_name]
            print(f"{delete_name} has been successfully deleted.")
        else:
            print(f"Error: {delete_name} not found in the phonebook.")

    elif choice == "quit":
        # Exit the program
        print("Exiting program...")
        break

    else:
        print("Invalid choice, please try again.")
