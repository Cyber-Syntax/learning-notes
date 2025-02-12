# x = input("What's x: ")

# This can be usable too
# y = int(input("What's y: "))

# #z = x + y # output: 12 because we didn't do with integar
# z = int(x)+int(y)
# print(z)

# x = float(input("x: "))
# y = float(input("y: "))

# #z = round(x / y) # 2/3 = 0.66666666666
# z = round(x / y, 2) # 2/3 = 0.67

# #print(f"{z:,}") # 1,000 this is for comma
# print(f"{z:2f.}") # float


# I am tryed to do with functions


def main():
    x = int(input("x:"))
    print("x squared is", square(x))


def square(n):
    # return n * n # 9
    # return n ** 2 # 9
    return pow(n, 2)  # 3 ^ 2 = 9


main()
