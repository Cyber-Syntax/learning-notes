import argparse

# create an ArgumentParser object with a description of the script's purpose
parser = argparse.ArgumentParser(description="Meow like a cat")

# add an argument "-n" with a default value of 1, a help message, and a type of int
parser.add_argument("-n", default=1, help="number of times to meow", type=int)

# parse the command line arguments using the parse_args() method
args = parser.parse_args() # argparse import sys and figure out 

# use a for loop to print "meow" args.n times
#for _ in range(int(args.n)): # we write this up type=int to handle this
for _ in range(args.n):
    print("meow")
