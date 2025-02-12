# Write me values() python example. Explain code with comments for beginner. Write me beginner and real world scenerio. Relevant

# Beginner Scenario
# Suppose we want to create a dictionary that consists of the names of fruits and their corresponding colors.

fruit_colors = {
  "apple": "red",
  "banana": "yellow",
  "grapes": "green"
}

# To get the values from the dictionary, we can use the built-in values() method.

fruit_colors_values = fruit_colors.values()

# The values() method will return all the values in the dictionary as a list.
# So if we print the values we will get the following result:

print(fruit_colors_values)

# Output:
# ['red', 'yellow', 'green']

#Real-world Scenario
#Suppose we have a dictionary of employee details such as name and salary.

employee_salary = {
  "John": 50000,
  "Julia": 60000,
  "Ethan": 40000
}

# To get the salary details of the employees, we can use the values() method.

salary_values = employee_salary.values()

# The values() method will return a list of all the salaries in the dictionary.
# So if we print the values, we will get the following result:

print(salary_values)

# Output:
# [50000, 60000, 40000]