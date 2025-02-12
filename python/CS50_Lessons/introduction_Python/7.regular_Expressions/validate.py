email = input("email: ").strip()

username, domain = email.split("@")

if username and domain.endswith(".edu"):
    print("Valid")
else:
    print("Invalid")



# if "@" in email and "." in email:
#     print("Valid")
# else:
#     print("Invalid")    