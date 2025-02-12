# Initialize a string with tab characters
string = "Hello\tWorld"

# Replace the tab characters with 4 spaces
new_string = string.expandtabs(30)

# Print the new string
print(new_string)  # Output: "Hello    World"


# Another example 

# Initialize a list of strings
rows = ["ID\tName\tAge", "1\tAlice\t23", "2\tBob  \t27", "3\tCharlie\t32"]

# Replace the tab characters with 4 spaces
rows = [row.expandtabs(4) for row in rows]

# Print the formatted rows
for row in rows:
    print(row)
