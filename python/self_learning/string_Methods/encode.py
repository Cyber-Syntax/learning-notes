# Encode a string using the UTF-8 encoding

string = "Hello World!"

# Encode the string as a sequence of bytes using the UTF-8 encoding
encoded_string = string.encode("utf-8")

# Print the encoded string
print(encoded_string)  # outputs b'Hello World!'


# real world example:


# Encode a string as a sequence of bytes using the UTF-8 encoding

string = "Hello World!"

# Encode the string as a sequence of bytes using the UTF-8 encoding
encoded_string = string.encode("utf-8")

# Upload the encoded string to a server
response = upload_to_server(encoded_string)

# Check the response from the server
if response.status_code == 200:
    print("The string was successfully uploaded to the server.")
else:
    print("There was an error uploading the string to the server.")


# Another example:


# Encode a string as a sequence of bytes using the Base64 encoding

string = "Hello World!"

# Encode the string as a sequence of bytes using the Base64 encoding
encoded_string = string.encode("base64")

# Send the encoded string in an email
send_email("recipient@example.com", "Encoded String", encoded_string)

# Print a confirmation message
print("The encoded string was sent in an email to recipient@example.com.")
