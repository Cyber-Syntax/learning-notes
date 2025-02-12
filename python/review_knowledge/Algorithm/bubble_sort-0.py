arr = [64, 34, 25, 12, 22, 11, 90]
n = len(arr) # Get the length of the array

print("n = ", n) # n = 7
for i in range(n): # i starting from 0 to (n - 1)
    # testing what is going on in the loop
    print("i = ", i) # i = 0, 1, 2, 3, 4, 5, 6
    
    # Last i element are already in place (Numbers 0 to 6 are already in place)
    for j in range(0, n - i - 1): # j starting from 0 to (n - i - 1) 7 - 0 - 1 = 6,
                                  # which means j = 0, 1, 2, 3, 4, 5
                                  # range(0, 6) = 0, 1, 2, 3, 4, 5
        print("j = ", j) 
        # Traverse the array from 0 to n-i-1
        # Swap if the element found is greater 
        # than the next element
        if arr[j] > arr[j + 1]:
            print("arr[j] = ", arr[j])
            arr[j], arr[j + 1] = arr[j + 1], arr[j] # Swap the elements
            print("arr[j] = ", arr[j])
            swapped = True
    if (swapped == False):
        break

print("Sorted array is:")
for i in range(len(arr)):
    print("%d" % arr[i], end=" ")
