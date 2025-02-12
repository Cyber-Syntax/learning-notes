# My code:
def inRange(x, y):
    if x < 1/3 < y:
        return True
    else:
        return False

print(inRange(2, 3))

# Less code:
def inRange(x, y):
  return (x < 1/3 < y)

print(inRange(-1, 3))
print(inRange(2, 3))