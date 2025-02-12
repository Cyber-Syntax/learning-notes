string = "Hello World!"
parts = string.rsplit()
print(parts) 

string = "Hello-World-New-sentences/trying-isitjustone"
parts = string.rsplit("-")
print(parts) # ['Hello', 'World', 'New', 'sentences/trying', 'isitjustone']


# split vs rsplit


string = "Hello-World-New-sentences/trying-isitjustone"

# Split the string at all occurrences of "-" using split()
# it starts from the left side of the string 
parts = string.split("-")
print(parts)

# Split the string at all occurrences of "-" using rsplit()
# it starts from the right side of the string 
parts = string.rsplit("-")
print(parts)


string = "Hello-World-New-sentences/trying-isitjustone"

# Split the string at the first occurrence of "-" using split()
parts = string.split("-", 1)
print(parts)

# Split the string at the first occurrence of "-" using rsplit()
parts = string.rsplit("-", 1)
print(parts)
# Output:
# ['Hello', 'World-New-sentences/trying-isitjustone']
# ['Hello-World-New-sentences/trying', 'isitjustone']


# split 


items = 'apples, oranges, bananas, grapes'

item_list = items.split(', ')
print(item_list)



string = "Hello-World-New-sentences/trying-isitjustone"

# Split the string at the first occurrence of "-" using split()
parts = string.split("-", 1)
print(parts)

# Split the string at the first occurrence of "-" using rsplit()
parts = string.rsplit("-", 1)
print(parts)
# Output:
# ['Hello', 'World-New-sentences/trying-isitjustone']
# ['Hello-World-New-sentences/trying', 'isitjustone']
