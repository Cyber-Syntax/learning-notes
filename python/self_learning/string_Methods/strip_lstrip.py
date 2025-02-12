phone_numbers = [' 555-555-1212 ', ' 555-555-1213', '555-555-1214 ']

formatted_numbers = [number.strip() for number in phone_numbers]
print(formatted_numbers)

# Output: ['555-555-1212', '555-555-1213', '555-555-1214']

# l.strip same
file_paths = [' /home/user/documents/ ', ' /home/user/downloads/', '   /home/user/images/']

formatted_paths = [path.lstrip() for path in file_paths]
print(formatted_paths)


string = '######Hello World######'
stripped_string = string.lstrip('#')
print(stripped_string)


string = '   Hello World   '
stripped_string = string.strip()
lstripped_string = string.lstrip()

print(stripped_string)
print(lstripped_string)

#Output: 'Hello World' -> delete all the emptys
#        'Hello World  ' -> just delete left side
