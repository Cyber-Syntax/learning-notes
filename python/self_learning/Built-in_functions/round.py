x = round(3.14159, 2)
print(x) # prints 3.14

# real-world cybersecurity example

import hashlib
import math

import hashlib
import math

def hash_password(password):
  # Use the round() function to round the password length to the nearest integer
  password_length = round(len(password))

  # Use the SHA-256 hashing algorithm to hash the password
  hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()

  # Remove the round() function, as it cannot be used on a string value
  # hashed_password = round(hashed_password, -1)
 
  return hashed_password

password = input("Enter your password for hashing: ")

# Test the password hashing function
hashed_password = hash_password(password)
print("This is your hashed password:\n",hashed_password) # Prints the hashed password

