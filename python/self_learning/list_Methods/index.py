# Write me index() python example for beginner
# with explaining code with comments and give me beginner and advanced real world scenerio

# Beginner Example
# This example uses the index() method to find the index of the first occurrence of an item in a list.

# Create a list of fruits
fruits = ["apple", "banana", "cherry"]

# Use index() to find the index of "apple"
apple_index = fruits.index("apple")

# Print the index of "apple"
print(apple_index)

# Output: 0 - "apple" is at index 0 in the list.

# Beginner Real World Scenario
# You are making a smoothie and you have a list of the ingredients you need.
# You want to know which item is at the beginning of the list so you use the index() method to find the index of the first item.

# Advanced Example
# This example uses the index() method to find the index of the last occurrence of an item in a list.
# Bu örnek, bir listedeki bir öğenin son geçtiği dizinin dizinini bulmak için index() yöntemini kullanır.

# Create a list of fruits
fruits = ["apple", "banana", "cherry", "apple", "banana"]
# 0-1-2-3-4 
# Use index() to find the index of the last occurrence of "banana"
# The len(fruits) function returns the length of the list fruits.
# The fruits[::-1] syntax creates a new list that is a reversed copy of the original list.
# The ::-1 slice notation means to start at the end of the list and go to the beginning, step by step.
# The -1 at the end of the expression subtracts 1 from the index.
# İfadenin sonundaki -1, dizinden 1 çıkarır.
# The last_banana_index variable stores the result of the expression(ifade).
first_banana_index = fruits.index("banana")
last_banana_index = len(fruits) - fruits[::-1].index("banana") -1

# Print the index of the last occurrence of "banana"
print(last_banana_index)
print(first_banana_index)
# Output: 4 - "banana" is at index 4 in the list.
# Çıktı: 4 - "muz" listede dizin 4'te.

