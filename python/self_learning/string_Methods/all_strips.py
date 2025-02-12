# Strip leading and trailing underscores from a string
string = "__This is a string with leading and trailing underscores__"

# Use the strip() function to remove the leading and trailing underscores
stripped = string.strip('_')
print(f"strip(): {stripped}")

# Use the lstrip() function to remove the leading underscores
left_stripped = string.lstrip('_')
print(f"lstrip(): {left_stripped}")

# Use the rstrip() function to remove the trailing underscores
right_stripped = string.rstrip('_')
print(f"rstrip(): {right_stripped}")

# Output:
# strip(): This is a string with leading and trailing underscores
# lstrip(): This is a string with leading and trailing underscores__
# rstrip(): __This is a string with leading and trailing underscores
