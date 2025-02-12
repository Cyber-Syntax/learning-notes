import csv

students = []

# csv = comma sepearated values
with open("homes.csv") as file:
    #reader = csv.reader(file) # return list
    reader = csv.DictReader(file) # return dictionary
    #for name, house in reader:  # you can use with reader
    #    students.append({"name": name, "house": house})
    for row in reader:  # you can use with DictReader
        #students.append({"name": row["name"], "house": row["house"]})
        students.append(row)


# We are using lambda anon function "lambda" when we didn't want to define and use just one time.
for student in sorted(students, key=lambda student: student["name"]):
    # single quotes because you already used two quotes.
    print(f"{student['name']} is from {student['house']}")