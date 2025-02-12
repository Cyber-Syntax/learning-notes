# We are except(hariç) errors

# Ask user until write "integer"
while True:  
    # Take input(str) from user and convert int
    try:    
        x = str(input("x: "))
        #print(f"x is {x}")
        # we can use here break to decrease lines
        # but it's up to us
    # We can't use ValueError().
    except ValueError:
        print("x is not an integer")
    # solve "name" error with else
    else:
    # Name error
    # name 'x' is not defined without else
        #print(f"x is {x}")
        break

print(f"x is {x}")
