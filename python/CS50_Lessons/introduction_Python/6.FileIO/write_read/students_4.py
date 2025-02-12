students = []

with open("names.csv") as file:
    for line in file:                   
         name, house = line.rstrip().split(",")  
         student = {"name": name, "house": house}         
         students.append(student)


# We are using lambda anon function "lambda" when we didn't want to define and use just one time.
for student in sorted(students, key=lambda student: student["name"]):
    # single quotes because you already used two quotes.
    print(f"{student['name']} is in {student['house']}")