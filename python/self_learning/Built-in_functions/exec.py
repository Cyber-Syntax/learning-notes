# Ask the user to input a mathematical expression
expression = input("Enter a mathematical expression: ")

# Evaluate the expression
exec("result = " + expression)

# Print the result
print("Result:", result)
