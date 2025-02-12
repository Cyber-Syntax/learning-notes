def findMaximum(list):   
    maximum = list[0]   
    for x in list:  
      if x > maximum:   
          maximum = x
    return maximum

list=[12, 24, 374, 4, 54]
# Call the function 'findMaximum' and print the result
print(findMaximum(list))

def findMaximumValueIndex(list):
    maximum = list[0]
    index = 0
    # For each index and value in the list using 'enumerate' function
    for i, value in enumerate(list):
        if value > maximum:
          maximum = value 
          index = i
    return [index, maximum]

list = [1, 2, 7, 4, 5]    
# Call the function 'findMaximumValueIndex' and assign the result to a list
[index, maximum] = findMaximumValueIndex(list)

print("Index:", index)
print("Maximum Value:", maximum)
