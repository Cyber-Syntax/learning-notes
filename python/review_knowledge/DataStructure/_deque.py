import collections

de = collections.deque([1,2,3,4,5])
print(de) # deque([1, 2, 3, 4, 5])

de.append(6)
print("Append 6: ", de) # deque([1, 2, 3, 4, 5, 6])

de.appendleft(0)
print("Appendleft 0: ", de) # deque([0, 1, 2, 3, 4, 5, 6])

de.pop()
print("Pop: ", de) # deque([0, 1, 2, 3, 4, 5])

de.popleft()
print("Popleft: ", de) # deque([1, 2, 3, 4, 5])

de.clear()
print("Clear: ", de) # deque([])

de.extend([1,2,3])
print("Extend: ", de) # deque([1, 2, 3])

de.extendleft([0])
print("Extendleft: ", de) # deque([0, 1, 2, 3])

de.rotate(1)
print("Rotate 1: ", de) # deque([3, 0, 1, 2])

de.rotate(-1)
print("Rotate -1: ", de) # deque([0, 1, 2, 3])

de.reverse()
print("Reverse: ", de) # deque([3, 2, 1, 0])

de.count(1)
print("count(1): ", de.count(1)) # 1

de.index(1)
print("Index 1: ", de) # deque([3, 2, 1, 0])

de.remove(1)
print("Remove 1: ", de) # deque([3, 2, 0])

# len
print("Len: ", len(de)) # 3

# index
print("deque: ", de) # deque([3, 2, 0])")
print("Index 2: ", de.index(2)) # 1

# insert
de.insert(1, 1)
print("Insert(1, 1): ", de) # deque([3, 1, 2, 0])

