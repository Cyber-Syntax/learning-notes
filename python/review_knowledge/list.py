def getSquare():
    l1=[ x ** 2 for x in range(21) if x % 3 != 0 and x % 2 == 0]
    return l1

print(getSquare()) # [4, 16, 64, 100, 196, 256, 400]

def append():
    l2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    result = []
    for i in range(len(l2) -1, -1, -1): # range(start, stop, step)
        result.append(l2[i])
    return result

print(append()) # [9, 8, 7, 6, 5, 4, 3, 2, 1]

# Look list is sorted or not
def isSorted():
    l3 = [1, 2, 5, 4]
    print(l3)
    for i in range(len(l3) - 1): # range(3) = [0, 1, 2]
        num = l3[i] 
        next_num = l3[i + 1]
        if num > next_num: # 1 > 2
            return False
    return True

print("Is it sorted?", isSorted()) # False

def is_sorted():
    l4 = [1, 2, 5, 4]
    print(l4)
    return sorted(l4) == l4

print("Is it sorted?", is_sorted()) # False

def is_sorted2():
    l5 = [1, 2, 3, 4]
    print(l5)
    return all(l5[i] <= l5[i + 1] for i in range(len(l5) - 1))

print("Is it sorted?", is_sorted2()) # True