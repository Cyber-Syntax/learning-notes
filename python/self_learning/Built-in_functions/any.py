def check_password_strength(password):
    # Set the initial score to 0
    score = 0

    # Check the password length and increase the score for longer passwords
    if len(password) >= 8:
        score += 1

    # Check for the presence of uppercase and lowercase letters, numbers, and 
    # special characters, and increase the score for each one found
    # Bu kod, bir password adlı değişkenin içeriğinde en az bir büyük 
    # harf olup olmadığını kontrol eder. 
    if any(c.isupper() for c in password):
        score += 1
    if any(c.islower() for c in password):
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(c in SPECIAL_CHARS for c in password):
        score += 1

    return score

# Another example

# A list of booleans
booleans = [True, False, True]

# Use any() to check if at least one element is True
if any(booleans):
  print("At least one element is True")
else:
  print("All elements are False")

# Output: At least one element is True
