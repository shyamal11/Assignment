students = input("Enter student names separated by commas: ").strip().split(', ')
subjects = input("Enter subjects separated by commas: ").strip().split(', ')

student_subject_dict = {}
for i in range(len(students)):
    student_subject_dict[students[i]] = subjects[i]

print(f"Dictionary using for loops: {student_subject_dict}")

student_subject_dict_comprehension = {students[i]: subjects[i] for i in range(len(students))}

print(f"Dictionary using dictionary comprehension: {student_subject_dict_comprehension}")
