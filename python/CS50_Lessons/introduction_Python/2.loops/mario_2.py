def main():
    print_square(3)  # kare alma
    print_triangle(3)

# Creating 3x3 brick in mario
def print_square(size):
    # For each row in square
    # Create column and go j to create row
    for i in range(size):
        # For each brick in row
        # Create 3 row and go i to create new line
        for j in range(size):
            # Print Brick
            print("#", end="")
        # We are using because of add new line
        # Creating 3 brick ### and going to print that
        # Create 3 row and go i, Create 3 row and go i
        print()

# My mistake
""" 
def print_triangle(size):
    for i in range(size):
        i -= 1        
        for j in range(size):            
            j -= 1
            print("*", end="")
        print() 
"""
# openai
def print_triangle(size):
    for i in range(size):
        for j in range(i+1):
            print("*", end="")
        print()

# openai triangle
for i in range(1,11):
    print('*' * i)

main()
