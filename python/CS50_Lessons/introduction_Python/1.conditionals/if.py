def check_numbers(x,y):
    # Check numbers if they number or not
    if not isinstance(x, int) and isinstance(y, int):
        print("They are not number")
    else:
        # Other codes
        if x < y:
            print("y greater")
        elif x > y:
            print("x greater")
        elif x == y:
            print("They are equal")
        else:
            print("Unkown error.")

# 'A' is not equal to the number 65.
# this does not mean that the character 'A' is equal to the number 65.
# the number 65 is an integer representing the decimal value 65

# Take input from user
x = "A"

y = "Z"

# Start our defined function to start code
check_numbers(x, y)            


# My mistakes

    # if x == int or y == int: # WRONG because
# they are gonna always be False, x not the int type itself
    # float method isn't necessary, because
    # x and y are already numbers(int or float)
        #x.__float__()
        #y.__float__()



