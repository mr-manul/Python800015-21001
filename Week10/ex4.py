class Student:
    def __init__(self, id, name, score):
        self.id = id
        self.name = name
        self.score = score

student_list = []

student1 = Student(12, "M1", 20)
student_list.append(student1)

student2 = Student(12, "M2", 20)
student_list.append(student2)

student3 = Student(12, "M3", 20)
student_list.append(student3)

print([student.name for student in student_list])
print([student.id for student in student_list])
print([student.score for student in student_list])

highest_score_student = max(student_list, key=lambda student: student.score)
print(f"The student with the highest score is {highest_score_student.name} with a score of {highest_score_student.score}.")