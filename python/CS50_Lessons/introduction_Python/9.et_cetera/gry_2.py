students = ["Hermione", "Harry", "Ron"]

#list comprehension
grys = [{"name": student, "house": "Gry"} for student in students]
print(grys)
# dictionary comprehension
grys = {student: "Gry" for student in students}


print(grys)