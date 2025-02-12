import os

# Find the path for file.
file_path = "my_file.txt"

absolute_path = os.path.abspath(file_path)

print(absolute_path)  # Output: /Users/username/my_file.txt (or similar)
