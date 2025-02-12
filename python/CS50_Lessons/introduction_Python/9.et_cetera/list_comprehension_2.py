students = [
    {"name": "Hermione", "house": "Gry", "patronus": "Otter"},
    {"name": "Yoda", "house": "Gry", "patronus": "Magic"},
    {"name": "Ron", "house": "Gry", "patronus": "Dog"},
    {"name": "Droco", "house": "Sly", "patronus": None},
]


def is_gry(s):
    return s["house"] == "Gry"


grys = filter(is_gry, students)

for gry in sorted(grys, key=lambda s: s["name"]):
    print(gry["name"])
