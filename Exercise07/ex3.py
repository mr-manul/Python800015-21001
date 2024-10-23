students = {}

for i in range(3):
    name = input(f"Enter the name of student {i + 1}: ")

    math = int(input(f"Enter {name}'s math score: "))
    science = int(input(f"Enter {name}'s science score: "))
    history = int(input(f"Enter {name}'s history score: "))

    students[name] = {
        'math': math,
        'science': science,
        'history': history
    }

highest_total = 0
top_student = ""

for name, scores in students.items():
    total_score = scores['math'] + scores['science'] + scores['history']

    if total_score > highest_total:
        highest_total = total_score
        top_student = name

print(f"\nThe student with the highest total score is {top_student} with a score of {highest_total}.")
