import sys

# check if there are no arguments passed to the script # betiğe iletilen herhangi bir argüman olup olmadığını kontrol edin
if len(sys.argv) == 1:
    # if no arguments are passed, just print "meow"
    print("meow")

# check if there are 3 arguments passed to the script and the second argument is "-n"
elif len(sys.argv) == 3 and sys.argv[1] == "-n":
    # if both conditions are true, store the third argument as an integer in the variable "n"
    n = int(sys.argv[2])
    # use a for loop to print "meow" n times
    for _ in range(n):
        print("meow")

# if the conditions above are not met(karşılanmazsa), print the usage message
else:
    print("usage: meows.py")