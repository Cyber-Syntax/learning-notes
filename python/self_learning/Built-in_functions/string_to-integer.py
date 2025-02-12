# We are doing this because input didn't know what is the integar. It's taking everything string also "123" to.

# Ask the user to input their age
age_string = input("Enter your age: ")

# Convert the age string to an integer
age = int(age_string)

# Check if the age is a valid value (between 1 and 120)
if age < 1 or age > 120:
    print("Error: Invalid age")
else:
    print("Your age is", age)