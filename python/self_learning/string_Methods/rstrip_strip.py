email_list = ['   user1@example.com  ', 'user2@example.com', ' user3@example.com  ']

for i, email in enumerate(email_list):
    email_list[i] = email.strip()  # remove leading and trailing whitespace from the email

# Now the email_list looks like this: ['user1@example.com', 'user2@example.com', 'user3@example.com']


string = '   Hello World!   \n'

stripped_string = string.strip()
# stripped_string is now 'Hello World!'

rstripped_string = string.rstrip()
# rstripped_string is now '   Hello World!'



#  strip removes both leading and trailing whitespace characters from a string. This includes spaces, tabs, and newline characters.
#  rstrip only removes trailing whitespace characters from the right side of a string.