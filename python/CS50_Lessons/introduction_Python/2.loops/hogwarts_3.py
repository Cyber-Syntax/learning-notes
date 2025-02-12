# dictionary words: name, house, patronus
# dictionary definition or value: Hermione, Gry, Otter

# Dictionary can be in the list.
students = [
    {"name": "Hermione", "house": "Gry", "patronus": "Otter"},
    {"name": "Yoda", "house": "Gry", "patronus": "Magic"},
    {"name": "Ron", "house": "Gry", "patronus": "Dog"},
    {"name": "Droco", "house": "Sly", "patronus": None},
]
# for student in students:
# print(student["name"], student["house"],student["patronus"], sep=", ") # seperate with comma ","

def student_crendentials(name):
    for student in students:
        if student["name"] == name:
            return dict(student)

print(student_crendentials("Hermione"))