# Comments can be your to-do list.

"""
This is more comment in python.
succint = kısa ve öz
pseudocode = sözde kod
"""

# Take user name 
#user_name= input("What's your name: ")
user_name = "     david malan new account".title().strip()

# Remove whitespace from str'ing
#user_name = user_name.strip().title()

# Capitalize user's name like david to David
# It just using for first word
#user_name = user_name.capitalize()

# It's upper all words first 
#user_name = user_name.title()

# print hello to specific user with same line
# Better usage with plus "+" not with comma ",".
print("Hello! "+ user_name,"What's up?")

# but with other things, we need to use comma ","

# end default "\n"
print("Hello! ", end = "", sep="!!")
print(user_name)

# f-strings
# Can be use in the "quotes" and much better than other but can be change for case.
print(f"Hello! {user_name} What's up?") 

# separator
print("Hello", user_name, sep="!!") # Output: Hello!!David Malan New Account

# this is the print defaults:
# print(*objects, sep=' ', end='\n', file=None, flush=False)
# Reference python.org

# quotes printing
print("Hello, \"friend\"") # Output: Hello, "friend"