s = "this is a string"
print(s.title())  # Output: "This Is A String"


s = "this is a string"
print(title(s))  # Output: "This Is A String"


# difference

s = "this is a string"

# Using the title() method
t1 = s.title()
print(t1)  # Output: "This Is A String"

# Using the built-in title() function
t2 = title(s)
print(t2)  # Output: "This Is A String"

print(s)  # Output: "this is a string" (original string is unchanged)
print(t1)  # Output: "This Is A String" (modified string is unchanged)
print(t2)  # Output: "This Is A String" (modified string is unchanged)


# istitle 
# the main difference between these two methods is that title() is used to manipulate the capitalization of a string, while istitle() is used to check whether a string is in title case.
# >>> "Hello World".istitle()
# True
# >>> "hello world".istitle()
# False
# >>> "Hello world".istitle()
# False
