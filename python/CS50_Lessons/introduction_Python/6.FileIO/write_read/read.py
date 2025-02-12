names = []
# We are using .csv, when we use excel etc.
with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip().title())

for name in sorted(names):
    print(f"hello, {name}")