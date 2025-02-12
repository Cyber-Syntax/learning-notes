# Define a list of user accounts
accounts = [
    {"username": "johnsmith"},
    {"username": "sarahjones"},
    {"username": "johndoe"},
    {"username": "janedoe"},
]

# Use the frozenset() function to create a set of usernames from the list of accounts
usernames = frozenset([account["username"] for account in accounts])

# Loop through the list of accounts and check if the username is already in the set of usernames
for account in accounts:
    username = account["username"]
    if username in usernames:
        print("The username '{}' is already taken. Please choose a different username.")
    else:
        print("The username '{}' is available.")
