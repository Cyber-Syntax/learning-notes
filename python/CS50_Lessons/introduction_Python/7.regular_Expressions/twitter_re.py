import re

url = input("URL: ").strip()

# ignorecase -> ignore uppercase
username = re.sub("^(https?://)?(www\.)?twitter\.com", "", url, re.IGNORECASE)

print(f"Username: {username}")