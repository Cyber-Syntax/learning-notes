import re

url = input("URL: ").strip()

if matches := re.search(r"^(https?://)?(?:www\.)?twitter\.(?:com|org)/([a-z0-9?]+)", url, re.IGNORECASE):
    #if matches.group(1) == "com":
    print(f"Username:", matches.group(1))