students = []

with open("names.csv") as file:
    for line in file:                   
         name, house = line.rstrip().split(",")
         student = {"name": name, "house": house}
         #student = {}
         #student["name"] = name
         #student["house"] = house
         students.append(student)

# geting student name
# We are using this for sorting A to Z # Also we can use this to sort house variable to
def get_name(student):
    return student["name"]

# We are using sorted with get_name defination because we can't use rstrip.split functions
# because we changed list file to dictionary in list file.
for student in sorted(students, key=get_name):
    # single quotes because you already used two quotes.
    print(f"{student['name']} is in {student['house']}")