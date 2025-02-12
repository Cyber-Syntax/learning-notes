# import modules
from sys import argv

""" Usage:
    - You need to start on terminal because of the IndexError. 
    Problems:
    - We need to give name. We can solve this error with give 0 but
    - It's tell us Hello my name is name.py while 0 
"""

# Check for errors
if len(argv) < 1:
    # Same function, It's up to developer, experience, apps...
    #print("Too few arguments")
    exit("Too few arguments")
elif len(argv) > 2:
    #print("Too many arguments")
    exit("Too many arguments")
#else:
    #print("Hello, my name is", argv[1])
    
print("Hello, my name is", argv[1])
    