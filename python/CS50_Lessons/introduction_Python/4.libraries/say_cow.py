# Do not same name your python code with modules. It's gonna give you error.

# importing modules
import cowsay
import sys

# We need to add name over 2 word
if len(sys.argv) == 2:
    #cowsay.cow("hello, " + sys.argv[1])
    cowsay.trex("Roarrrrrr, " + sys.argv[1])
else:
    print("To few arguments")
