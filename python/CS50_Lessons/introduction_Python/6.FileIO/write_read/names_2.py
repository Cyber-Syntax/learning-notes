name = input("What's your name: ")

# Write file
with open("names.txt", "a") as file:
    file.write(f"{name}" + "\n")
# Read file
with open("names.txt", "r") as file:
    lines = file.readlines()

# lines is a list, line is a variable
for line in lines:
    print("hello,", line, line.rstrip()) # end="" can be usable but strip best way to do that.




"""
#Write file
file = open("names.txt", "a") # w = write(?), a = append
# \n with f-string
file.write(f"{name}" + "\n")
file.close()
"""
