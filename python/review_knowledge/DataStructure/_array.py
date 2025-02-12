import array as arr
# Do not name your file array.py or you will overwrite Python's array module.

# How you would create an array that contains the values 1, 2, 3, 4, and 5?
# arr.array(typecode, [1, 2, 3, 4, 5])
# typecode: Type code of the array. For example, if you want an array of integers, you can use i.
# float – ‘f’, double – ‘d’, character – ‘c’, integer – ‘i’ etc.
numbers = arr.array('i', [1, 2, 3])
print(numbers) # output = array('i', [1, 2, 3])

print("How would you print the first value of the array?")
print(numbers[0]) # output = 1

print("How would you print all the values of the array?")
for number in numbers:
    print(number) # output = 1, 2, 3

# This is not the best way to print all the values of the array. Use enumerate() instead. (Pylint suggestion)
print("How would you print all the values of the array with range and len?")
for number in range(len(numbers)):
    print(numbers[number]) # output = 1, 2, 3

# enumerate() method adds counter to an iterable and returns it (the enumerate object).
print("How would you print all the values of the array with their index?")
for number in enumerate(numbers):
    print(number) # output = (0, 1), (1, 2), (2, 3)

# index() method returns the index of the specified element in the array.
print("How would you find the index of the value 2?")
print(numbers.index(2))  # output = 1

# slice
print("How would you print the values 2, 3, and 4?")
print(numbers[1:4]) # output = array('i', [2, 3])

# Change an array element
print("How would you change the value 2 to 6?")
numbers[1] = 6
print(numbers) # output = array('i', [1, 6, 3])

# Append an element to an array
print("How would you append the value 7 to the array?")
numbers.append(7)
print(numbers) # output = array('i', [1, 6, 3, 7])

# Append more than one element at a time
print("How would you append the values 8 and 9 to the array?")
numbers.extend([8, 9])
print(numbers) # output = array('i', [1, 6, 3, 7, 8, 9])

# Insert an element at a specific position
print("How would you insert the value 4 at index 3?")
numbers.insert(3, 4)
print(numbers) # output = array('i', [1, 6, 3, 4, 7, 8, 9])

# Remove an element from an array
print("How would you remove the value 3 from the array?")
numbers.remove(3)
print(numbers) # output = array('i', [1, 6, 4, 7, 8, 9])

# Remove the last element from an array
print("How would you remove the last value from the array?")
numbers.pop(5) # index 5 = 9
print(numbers) # output = array('i', [1, 6, 4, 7, 8])
