# Parse a URL and extract the domain name
url = "https://www.example.com/path/to/page"

# Find the index of the last period in the URL
index = url.rfind(".")

# Extract the domain name
if index != -1:  # Make sure a period was found
    # Find the index of the second-to-last slash in the URL
    index = url.rfind("/", 0, index)

    # Extract the domain name
    if index != -1:  # Make sure a slash was found
        domain = url[index+1:url.rfind(".")]
        print(domain)  # "example"
    else:
        print("Domain not found")
else:
    print("Domain not found")
