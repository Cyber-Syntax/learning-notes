# How to meow with loops

i = 3
"""
if we use minus, it's gonna decrease i to 0.
if we use plus, it's gonna *upgrade* i to 3
"""
while i != 0:
    
    #While i not zero, meow.
    
    print("meow")
    # Loops gonna infinity without this
    # because "i" didn't finish.
    i = i - 1

while i <= 3:
    
    #while i lower or equal 3, rof.
    
    print("rof")
    # Loops gonna infinity(i - 1) without (i + 1)
    
    # If we use (i <= 3), it's gonna rof 4 times.
    i = i + 1
    # If we didn't use equal (i < 3), it's gonna rof 3 times.

j = 0
# When you use "=" loops gonna infinity.
""" but, if we don't use equal sembol on while(j < 3), it's gonna end 3 moo."""
while j < 3:
    print("moo")
    j += 1

# We can use range on for loops
# If you didn't want to use again you can give underscore for name
for _ in range(3):
    print("bark") # 1 bark * 3
    
    # end="\n" This is default to creating new line.
    print("meow\n" * 3, end="") # 3 meow * 3 meow

# proffessor example
while True:
    n = 3
    if n > 0:
        break
for _ in range(n):
    print("moo_2") # 3 moo_2
