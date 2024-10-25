#Exercise:
#get two string from a user and print all the indexes where the second
#string appears in the first string. If the second string is not found, print -1.

# Get two strings from the user
first_string = input("Enter the first string: ")
second_string = input("Enter the second string: ")

# Initialize a list to store the indexes
indexes = []

# Search for all occurrences of the second string in the first string
start = 0
while True:
    # Find the next occurrence of the second string
    index = first_string.find(second_string, start)

    # If no more occurrences are found, break the loop
    if index == -1:
        break

    # Add the index to the list
    indexes.append(index)

    # Move the start point forward to search for the next occurrence
    start = index + 1

# Print the indexes or -1 if the second string is not found
if indexes:
    print("Indexes:", indexes)
else:
    print(-1)
