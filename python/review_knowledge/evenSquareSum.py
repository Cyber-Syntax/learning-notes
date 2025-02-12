def evenSquareSum():  
  l1 = [(x * x) for x in range(21) if x % 2 == 0] # even number list
  return sum(l1)
print(evenSquareSum())

def getSquare():
 l1=[ x ** 2 for x in range(0, 21) if x % 3 != 0 and x % 2 == 0] # "if" may or may not be.
 return l1
print(getSquare())

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(4)) # 5

def sum_N_Numbers(n):
    if n <= 1:
        return n
    else:
        return n + sum_N_Numbers(n-1) # 5 + 4 + 3 + 2 + 1     
print(sum_N_Numbers(5))

def favoriteBook(title, author):
    return f"My favorite book is {title} by {author}.".title()
print(favoriteBook("The Alchemist", "Paulo Coelho"))
