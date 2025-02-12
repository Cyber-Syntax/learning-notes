names = []

for _ in range(3):
    # names.append(input("Whats your name: ")) # It can be like this too.
    name = input("Whats your name: ")
    names.append(name)
    
for name in sorted(names):
    print(f"hello, {name}")

