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

print("\nStudents with a total score greater than 100:")

found = False

for name, scores in students.items():
    total_score = scores['math'] + scores['science'] + scores['history']

    if total_score > 100:
        print(f"{name}: Total score = {total_score}")
        found = True

if not found:
    print("No student has a total score greater than 100.")
