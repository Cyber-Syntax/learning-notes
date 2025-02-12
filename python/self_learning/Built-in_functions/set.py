# Create a new set to store unique IP addresses
ip_addresses = set()

# Add some IP addresses to the set
ip_addresses.add("192.168.0.1")
ip_addresses.add("10.0.0.1")
ip_addresses.add("172.16.0.1")

# Print the contents of the set
print(ip_addresses) # Prints {'192.168.0.1', '10.0.0.1', '172.16.0.1'}

# Attempt to add a duplicate IP address
# When a duplicate IP address is added to the set, it is not added again,
#  because sets only allow unique elements. 
ip_addresses.add("172.16.0.1")

# Print the contents of the set again
print(ip_addresses) # Prints {'192.168.0.1', '10.0.0.1', '172.16.0.1'}


# Another example:


# Create a new set to store unique user accounts
user_accounts = set()

# Add some user accounts to the set
user_accounts.add("user1")
user_accounts.add("user2")
user_accounts.add("user3")

# Print the contents of the set
print(user_accounts) # Prints {'user1', 'user2', 'user3'}

# Attempt to add a duplicate user account
user_accounts.add("user3")

# Print the contents of the set again
print(user_accounts) # Prints {'user1', 'user2', 'user3'}


# I didn't used for, if with set().

# Create a new set to store unique user accounts
user_accounts = set()

# Add some user accounts to the set
user_accounts.add("user1")
user_accounts.add("user2")
user_accounts.add("user3")

# Print the contents of the set
print(user_accounts) # Prints {'user1', 'user2', 'user3'}

# Define a list of user accounts to check
user_list = ["user1", "user2", "user3", "user4", "2.example"]

# Iterate over the list of user accounts
for user in user_list:
    # Check if the user account already exists in the set
    if user in user_accounts:
        print(f"The user account {user} already exists.")
    else:
        # Add the user account to the set
        user_accounts.add(user)
        # Print the contents of the set again
        print(user_accounts) # Prints {'user1', '


# Okay, I find the code what I want

# Create a new set to store unique user accounts
user_accounts = set()

# Add some user accounts to the set
user_accounts.add("user1")
user_accounts.add("user2")
user_accounts.add("user3")

# Print the contents of the set
print(user_accounts) # Prints {'user1', 'user2', 'user3'}

# Define a user account to check
# You can add this to input too
# user = input("Add user:", user_accounts) -> WRONG
user = input("Add user:")
#user = "user3"

# Check if the user account already exists in the set
if user in user_accounts:
    print(f"The user account {user} already exists.")
else:
    # Add the user account to the set
    user_accounts.add(user)
    # Print the contents of the set again
    print(user_accounts) # Prints {'user1', 'user2', 'user3'}
