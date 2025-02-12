#name = "Ron"

# if name == "Harry" or name == "Ron" or name == "Dracula":
#    print("Gryffindor")
# else:
#    print("Who?")

# This isn't usable in python
# match (name):
#     case ("Harry" | "Rom" | "Draco"):
#         print("Gry")
#     case ("Ron"):
#         print("Gry")
#     # like else
#     case (_):
#         print("Who?")

# Python uses if and elif (short for "else if") statements to perform conditional execution of code.
def match(name):
    if name == "Harry" or name == "Rom" or name == "Draco":
        print("Gry")
    elif name == "Draco":
        print("Something else")
    else:
        print("Who?")

match("Harry")  # prints "Gry"
match("Ron")  # prints "Gry"
match("Draco")  # prints "Gry"
match("Hermione")  # prints "Who?"
