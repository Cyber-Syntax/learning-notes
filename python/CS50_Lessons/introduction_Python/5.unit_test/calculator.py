# define main code
def main():
    # ask user input
    # x = int(input("x: "))
    x = input("x: ")
    # print squared(kare) x
    print("x squared is", square(x))


# define square
def square(n):
    # do square
    return n * n


# call main for start to code
# When we use this library different code, we don't want to call main all the time.
if __name__ == "__main__":
    main()
