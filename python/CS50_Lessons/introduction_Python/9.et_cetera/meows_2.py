# def meow(n: int) -> None: # catch error with mypy this -> None or -> str or etc.
#     for _ in range(n):
#         print("meow")
# (n: int) -> n = integer number, 
# returning str = "meow\n"  
def meow(n: int) -> str:
    """
    This function will take in an integer n and return a string of n meows, one per line.
    If n is not an int, a TypeError will be raised.
    
    :param n: Number of times to meow
    :type n: int
    :raise TypeError: If n is not an int
    :return: A string of n meows, one per line
    :rtype: str
    """
    
    # multiply the string "meow\n" by n and return the result
    return "meow\n" * n

# get user input and store it in the variable "number" as an int
number: int = int(input("Number: "))

# call the meow function with the user input as an argument and store the result in the variable "meows"
meows: str = meow(number) 

# print the value stored in the "meows" variable
print(meows) 
