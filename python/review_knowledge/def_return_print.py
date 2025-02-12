# My code:
def MathOp():
  a = 3 / 2
  b = 3 // 2
  c = 3 % 2
  d = 3**2
  return a,b,c,d
  
# Define returneds
[a,b,c,d] = MathOp()

print(a)
print(b)
print(c)
print(d)

# Golfed version

def MathOp():
  a = 3 / 2
  b = 3 // 2
  c = 3 % 2
  d = 3**2
  return a,b,c,d
  
print(*MathOp(), sep='\n')

"""
Explanation: This implementation uses the unpacking operator `*` to unpack the returned values from the function `MathOp`
into separate variables, which are then passed as arguments to the `print` function. The `sep` argument of the `print`
function is used to separate the output with a newline character. This  golfed version is shorter and more concise than 
the original, but it may  be less readable to someone unfamiliar with the unpacking operator.
"""

# Returning a tuple:

def MathOp():
  a = 3 / 2
  b = 3 // 2
  c = 3 % 2
  d = 3**2
  return a, b, c, d

result = MathOp()
print(result[0])
print(result[1])
print(result[2])
print(result[3])

# Returning a dictionary:

def MathOp():
  a = 3 / 2
  b = 3 // 2
  c = 3 % 2
  d = 3**2
  return {'a': a, 'b': b, 'c': c, 'd': d}

result = MathOp()
print(result['a'])
print(result['b'])
print(result['c'])
print(result['d'])