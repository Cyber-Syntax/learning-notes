def main():
    number = get_number()
    # adding number from user
    meow(number)

def meow(n):
    for _ in range(n):
        print("meow")

def get_number():
    while True:
        n = int(input("Number: "))
        # if n greater than 0
        if n > 0:
            # return just didn't stop function
            # It can be return value too.
            return n


main()