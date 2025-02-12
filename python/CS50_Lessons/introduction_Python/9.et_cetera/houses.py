# create a list of dictionaries representing students
students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Yoda", "house": "Gryffindor", "patronus": "Magic"},
    {"name": "Ron", "house": "Ravenslow", "patronus": "Dog"},    
    {"name": "Droco", "house": "Slytherin", "patronus": None},
]

# create an empty set to store the houses
houses = set()

# iterate over the students
for student in students:
    # if the student's house is not in the houses set, add it
    if student["house"] not in houses:
        houses.add(student["house"])

# sort the houses set and print the values
for house in sorted(houses):
    print(house) # print the house name
