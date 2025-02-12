# Write me fromkeys() python example for beginner
# with explaining code with comments and give me beginner and advanced real world scenerio


# Beginner
# The fromkeys() method creates a new dictionary from a given sequence of elements with a value provided by the user.
# fromkeys() yöntemi, kullanıcı tarafından sağlanan bir değerle belirli bir öğe dizisinden yeni bir sözlük oluşturur.

# Create a new dictionary with 3 elements
my_dict = dict.fromkeys(["name", "age", "gender"], "unknown")

# Print the dictionary
print(my_dict)

# Output: {'name': 'unknown', 'age': 'unknown', 'gender': 'unknown'}

# Advanced
# The fromkeys() method can be used to set a default value for a set of keys in a dictionary.

# Create a new dictionary with 3 elements
my_dict = dict.fromkeys(["name", "age", "gender"], "unknown")

# Set new values for the elements
my_dict["name"] = "John"
my_dict["age"] = 25
my_dict["gender"] = "Male"

# Print the dictionary
print(my_dict)

# Output: {'name': 'John', 'age': 25, 'gender': 'Male'}


# Real world 
student_names = {
    'John', 
    'Mary', 
    'Alex'
    }
# Create a dictionary with student names as keys and default values for grades
grades = dict.fromkeys(student_names, {'homework': 0, 'quiz': 0, 'test': 0})

print(grades)
# Output: {'John': {'homework': 0, 'quiz': 0, 'test': 0},
#          'Mary': {'homework': 0, 'quiz': 0, 'test': 0},
#          'Alex': {'homework': 0, 'quiz': 0, 'test': 0}}

# Update the grades for John
grades['John']['homework'] = 90
grades['John']['quiz'] = 85
grades['John']['test'] = 95

print(grades)
# Output: {'John': {'homework': 90, 'quiz': 85, 'test': 95},
#          'Mary': {'homework': 0, 'quiz': 0, 'test': 0},
#          'Alex': {'homework': 0, 'quiz': 0, 'test': 0}}
