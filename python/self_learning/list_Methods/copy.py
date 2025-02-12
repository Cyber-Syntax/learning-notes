# The copy() method is used to make a shallow copy of a list. It is a built-in function in Python that returns a copy of the given list.

# Beginner Scenario:

# Suppose you have a list of numbers and you want to make a copy of that list. You can use the copy() method to do this.

# example:

numbers = [1, 2, 3, 4]
numbers_2 = [5, 6, 7, 8]

# Use the append() method to add numbers_2 to numbers
all_numbers = numbers.copy()
all_numbers.append(numbers_2)
print("append:", all_numbers)

# Use the extend() method to add numbers_2 to numbers
all_numbers = numbers.copy()
all_numbers.extend(numbers_2)
print("extend:", all_numbers)




# Real World Scenario:

# Suppose you are organizing a birthday party and you want to make a list of guests to invite. You can use the copy() method to make a copy of this list so you can keep track of who has accepted the invitation and who has not.

# example:

# Suppose you have a list of guests
guests = ["John", "Sue", "Tom", "Kate"]

# Make a copy of the list
invited_guests = guests.copy()