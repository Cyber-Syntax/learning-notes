# Defining main to work with this code because if we define function upper all the time, It's gonna mess.
def main():
    hello()
    # lstrip -> just left rstirf -> just right strip -> all
    name = "     david                 ".lstrip().title().rstrip()

    hello(name)


# Define hello for use this all time for every user.
def hello(to="world!\n".title()):
    print("Hello", to, end="\n")

    # It's gonna give error because we didn't define name for this def
    # scope refers to a variable only existing in the context in which you defined it.
    # print("hello", name)


# Call main function to start codes.
main()
