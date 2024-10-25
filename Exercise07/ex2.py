dico = {}

while True:
    print("\nMenu: ")
    print("1. Input")
    print("2. Search")
    print("3. Delete")
    print("4. Quit")

    choice = input("Enter your choice: ").lower()

    if choice == "input":
        name = input("Enter name: ")
        number = input("Enter phone number: ")

        if name and number:
            dico[name] = number
            print(f"{name}'s phone number has been successfully added/updated.")
        else:
            print("Error: Name or phone number cannot be empty.")

    elif choice == "search":
        search_name = input("Enter name to search: ")
        if search_name in dico:
            print(f"Found user: {search_name}, Phone number: {dico[search_name]}")
        else:
            print(f"Error: {search_name} not found.")

    elif choice == "delete":
        delete_name = input("Enter name to delete: ")
        if delete_name in dico:
            del dico[delete_name]
            print(f"{delete_name} has been successfully deleted.")
        else:
            print(f"Error: {delete_name} not found.")

    elif choice == "quit":
        print("Exiting program...")
        break

    else:
        print("Error: Invalid choice, please choose again.")
