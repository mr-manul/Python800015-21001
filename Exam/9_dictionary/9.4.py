# Exercise:
# Get the names of three students and their math, science, and history scores.
# Print the name of the student with the highest total score.

# Initialize an empty dictionary to store student data
students = {}

# Get data for three students
for i in range(3):
    name = input(f"Enter the name of student {i + 1}: ")

    # Get scores for each subject
    math = int(input(f"Enter {name}'s math score: "))
    science = int(input(f"Enter {name}'s science score: "))
    history = int(input(f"Enter {name}'s history score: "))

    # Store the student's scores in the dictionary
    students[name] = {
        'math': math,
        'science': science,
        'history': history
    }

# Initialize variables to find the student with the highest total score
highest_total = 0
top_student = ""

# Iterate through the students to find the one with the highest total score
for name, scores in students.items():
    # Calculate the total score for the current student
    total_score = scores['math'] + scores['science'] + scores['history']

    # Check if this student has the highest total score so far
    if total_score > highest_total:
        highest_total = total_score
        top_student = name

# Print the name of the student with the highest score
print(f"\nThe student with the highest total score is {top_student} with a score of {highest_total}.")
