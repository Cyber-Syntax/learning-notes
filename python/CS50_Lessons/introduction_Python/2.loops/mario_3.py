# More clear way to do that.
def main():
    print_square(3)

# Creating 3x3 brick in mario
# row = satır, column = sütun
def print_square(size):
  for i in range(size):
    print_row(size)

def print_row(width):
    print("#" * width) # * impact

main()