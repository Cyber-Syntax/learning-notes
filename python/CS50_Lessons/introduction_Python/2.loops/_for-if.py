# from open_ai
from typing import List

# define a function that takes in a list of integers and returns the largest integer
def find_largest(numbers: List[int]) -> int:
  # initialize a variable to store the largest number
  largest = numbers[0]
  # iterate through each number in the list
  for number in numbers:
    # if the current number is larger than the current largest number, update the largest number
    if number > largest:
      largest = number
  # return the largest number
  return largest

# test the function with a list of numbers
print(find_largest([1, 2, 3, 4, 5]))  # prints 5
