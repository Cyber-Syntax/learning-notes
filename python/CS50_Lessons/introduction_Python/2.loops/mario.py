# This is for the mario bricks codes.

"""
def main():
    print_column(3)


def print_column(height):
    print("#\n" * height, end="") # end default: "\n"

#    for _ in range(height):
#       print("#")

main()

"""
""" This is the score bricks in mario
Create whatever bricks to create brick """
def main():
    print_row(4) # column(sütun), row(satır)
    print_height(3)

# print row how much wanted from main code
def print_row(width):
    print("?" * width) # genişlik(yandan boy)

def print_height(height):
    """
    I was created triangle by myself.
    """
    for _ in range(height):
        print("?" * height)
        height -= 1

main()