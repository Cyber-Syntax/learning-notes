students = [
    {"name": "Hermione", "house": "Gry", "patronus": "Otter"},
    {"name": "Yoda", "house": "Gry", "patronus": "Magic"},
    {"name": "Ron", "house": "Gry", "patronus": "Dog"},
    {"name": "Droco", "house": "Sly", "patronus": None},
]

grys = [student["name"] for student in students if student["house"] == "Gry"]

for gry in sorted(grys):
    print(gry)
