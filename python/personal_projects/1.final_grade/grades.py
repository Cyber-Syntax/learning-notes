grades = {
    "AA": 84.01,
    "AB": 77.01,
    "BA": 71.01,
    "BB": 66.01,
    "BC": 61.01,
    "CB": 56.01,
    "CC": 50.01,
    "CD": 46.01,
    "DC": 40.01,
    "DD": 33.01,
    "FF": 1.01
}

# Prompt the user for a key and a value
key = input("Enter a key: ")
value = input("Enter a value: ")

# Update the value of the specified key
grades[key] = value

# Iterate over the dictionary
for key, value in grades.items():
    # If the key starts with "A", increase the value by 10
    if key[0] == "A":
        grades[key] = value + 10
    # If the key starts with "D", decrease the value by 10
    elif key[0] == "D":
        grades[key] = value - 10

print(grades)
