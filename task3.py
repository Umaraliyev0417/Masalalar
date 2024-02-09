students = {
  "Student 1": "Steve",
  "Student 2": "Becky",
  "Student 3": "John"
    }

def get_student_names(students):
    result = []
    for x in students.values():
        result.append(x)
    return sorted(result)

print(get_student_names(students))