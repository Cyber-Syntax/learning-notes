# you can look example for this repetitions in re module.
import re

email = input("email: ").strip()

# .* repetition
# ? why .com can't valid.
if re.search(r"^(\w+\.)+@(\w+\.)?\w+\.(com|edu|org)$", email):
    print("Valid")
else:
    print("Invalid")

