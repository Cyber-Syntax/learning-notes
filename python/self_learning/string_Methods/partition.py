email = "user@example.com"

# Extract the username and domain using partition
username, _, domain = email.partition("@")

print(username)  # "user"
print(domain)  # "example.com"


# Another example 

# Parse a file path and extract the file name and extension
file_path = "C:/Users/user/Documents/report.pdf"

# Extract the file name and extension using partition
file_name, _, file_ext = file_path.rpartition("/")

print(file_name)  # "C:/Users/user/Documents"
print(file_ext)  # ".pdf"


# Real-world example 

emails = ["user1@example.com", "user2@example.com", "user3@example.com"]

# Extract the username from each email address
usernames = []
for email in emails:
    username, _, _ = email.partition("@")
    usernames.append(username)

print(usernames)  # ["user1", "user2", "user3"]


emails = ["user1@example.com", "user2@example.com", "user3@example.com"]

# Extract the username from each email address using a list comprehension
usernames = [email.partition("@")[0] for email in emails]

print(usernames)  # ["user1", "user2", "user3"]
