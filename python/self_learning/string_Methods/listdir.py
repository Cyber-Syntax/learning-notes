import os

folder_list = os.listdir('/home/developer/Documents/Code/python/')

print("Python directory:")
for item in folder_list:
    print("- {}".format(item))

# You can also use the enumerate() function to add numbering to the list, like this:
import os

# List the contents of the current directory
contents = os.listdir()

# Print the contents of the directory in a numbered list
print("Contents of the current directory:")
for i, item in enumerate(contents):
    print("{}. {}".format(i + 1, item))
