# Exercise:
# Get a score (integer) and output a grade (A, B, C, D, or F).
# Grading scale:
# A: 100-80
# B: 79-60
# C: 59-40
# D: 39-20
# F: 19-0
# If an integer other than 0-100 is entered, output an error message.

# Get the score from the user
score = int(input("Enter the score (0-100): "))

# Check the score and output the corresponding grade
if 80 <= score <= 100:
    print("Grade: A")
elif 60 <= score <= 79:
    print("Grade: B")
elif 40 <= score <= 59:
    print("Grade: C")
elif 20 <= score <= 39:
    print("Grade: D")
elif 0 <= score <= 19:
    print("Grade: F")
else:
    print("Error: Invalid score entered. Please enter a score between 0 and 100.")
