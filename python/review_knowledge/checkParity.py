# My code
def checkParity(n):
    if n % 2 == 0:
        return 0
    else:
        return 1

print("Odd parity", checkParity(3))
print("Even parity", checkParity(2))

# Less code 
def checkParity(n):
  result = (n % 2) ## Update result according to the parity
  return result

print("Odd parity", checkParity(17))
print("Even parity", checkParity(16))

# This code won code golf
checkParity=lambda n:n%2

print("Odd parity", checkParity(3))
print("Even parity", checkParity(2))
