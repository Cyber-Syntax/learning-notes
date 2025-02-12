# import modules
from sys import argv
# !, Not working
# Check for errors
if len(argv) < 2:
    # Same function, It's up to developer, experience, apps...
    #print("Too few arguments")
    exit("Too few arguments")
elif len(argv) > 2:
    #print("Too many arguments")
    exit("Too many arguments")

# 1: -> Slice(dilim) list from list
# :-1 -> bir tane sağdan eksilt # subtract one right
for arg in argv[1:1]:
    print("Hello, my name is", argv[1])
    

    