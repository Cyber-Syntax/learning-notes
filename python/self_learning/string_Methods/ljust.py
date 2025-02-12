names = ['John', 'Jane', 'Bob', 'Alice']

for name in names:
    print(name.ljust(10), end=' ')
print()


for name in names:
    print(name.ljust(10, '-'), end=' ')
print()

for name in names:
    print(name.ljust(10, '*'), end=' ')
print()
