def reverse(list):
    # get the length of the list
    length = len(list)
    print(length)

    # Create a new list with the same length as the input list
    new_list = [None]*length

    # loop through each item in the input list
    for item in list:
        # decrement "lenght" by 1 each iteration
        length = length - 1 
        # assign the current item to the corresponding index in new_list
        new_list[length] = item
    # return the reversed new_list
    return new_list

list=[1,2,3,4,5]
print(reverse(list))