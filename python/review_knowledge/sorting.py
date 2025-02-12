# find to big number in the list and
# sort the list in ascending order
# TODO Ask AI to understand more clearly
list = [1, 2, 3, 4, 10, 9,8,7,5]
print("The list is: ", list)

def isSorted(list):
    for i in range(len(list) - 1):
        if list[i] > list[i + 1]:
            return False
    return True

print("The list is sorted: ", isSorted(list))

def sort_asc(list):
    for i in range(len(list)):
        for j in range(i+1, len(list)):
            if list[i] > list[j]:
                list[i], list[j] = list[j], list[i]
    return list
print("The list in ascending order: ", sort_asc(list))    

def isSorted_2(list):
  flag = 0
  i = 1
  while i < len(list): 
      if(list[i] < list[i - 1]): # compare with the previous element
          flag = 1
      i += 1
      
  if (not flag) : 
      return True 
  else : 
      return False 
print(isSorted_2([1,2,3,4,5]))
print(isSorted_2([1,2,5,4,2]))