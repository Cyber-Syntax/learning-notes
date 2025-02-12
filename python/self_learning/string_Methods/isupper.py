passwords = ['password1', 'PASSWORD2', 'p@ssword3']

for password in passwords:
    if not password.isupper():
        print(f"{password} does not contain an uppercase character.")
    else:
        print(f"{password} is valid.")
