# Write me sort() python example for beginner
# with explaining code with comments and give me beginner and advanced real world scenerio


# Beginner:
# Sorting a list of numbers

numbers = [5, 2, 1, 3, 4]

# sort() function sorts the list in ascending order(artan düzen)
numbers.sort()

print(numbers) # Output: [1, 2, 3, 4, 5]

# Advanced:
# Sorting a list of tuples by the second element of the tuple(demetler)
# Demetleri her bir demetin ikinci elemanına göre sırala

tuples = [('apple', 5), ('banana', 3), ('mango', 2), ('orange', 4)]

# Using the key parameter in the sort() function, we can specify the index of the tuple element to sort by

# ascending order
# tuples.sort(key=lambda x: x[1])

# descending order
tuples.sort(key=lambda x: x[1], reverse=True)

print(tuples) # Output: [('mango', 2), ('banana', 3), ('orange', 4), ('apple', 5)]
