def ListofEvenOdds():
  l1 = []
  l2 = []  
  
  l1 = [x for x in range(0, 21) if (x % 2 == 0)]
  l2 = [x for x in range(0, 21) if (x not in l1)]
  return[l1, l2]
# decrease lines with if else or anything

def getSquare():
 l1=[x ** 2 for x in range(0, 21) if x % 3 != 0 and "if" x % 2 == 0] # "if" may or may not be.
 return l1 # [4, 16, 64, 100, 196, 256, 400]
 
print(getSquare())

