# create a bytes object
# the b character before the string indicates that the string 
# is a bytes object in Python.
data = b'hello world'

# create a memory view object
view = memoryview(data)

# access the data in the memory view
print(view[0])  # prints 104
print(view[1])  # prints 101
print(view[2])  # prints 108


# Another example

# create a bytes object from a file
with open('myfile.txt', 'rb') as f:
    data = f.read()

# create a memory view object
view = memoryview(data)

# access the data in the memory view
for i in range(10):
    print(view[i])
