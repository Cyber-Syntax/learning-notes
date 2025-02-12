import sys

from sayings import goodbye, hello 

# if arguments bigger than 2, print 
if len(sys.argv) == 2:
    goodbye(sys.argv[1])
else:
    print("To few arguments")
