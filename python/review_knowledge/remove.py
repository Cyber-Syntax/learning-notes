# remove list item with index
def removeList_index():
    l1 = [6, 8, 7]    
    l1.remove(l1[0])
    return l1

print(removeList_index())


# remove list item with for loop
def removeList_for():
    l1 = [1, 4, 5]
    l2 = [1]
    for delete in l2:
        l1.remove(delete)
    return l1

print(removeList_for())