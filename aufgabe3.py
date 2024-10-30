user_input = input("Enter a string: ")

clean = user_input.replace(".", "").replace(",", "").lower()

words = clean.split()

unique = set(word for word in words)

print("Number of Unique words:", len(unique))