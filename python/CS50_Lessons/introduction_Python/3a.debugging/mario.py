# define main code
def main():
    # Error handling with while
    while True:
        try:
            # ask user pyramid height
            height = int(input(("Height: ")))
            pyramid(height)
            # stop code when user give true input
            break
        # return main user question again and again.
        except ValueError:
            return main()


def pyramid(n):
    for i in range(n):
        print(i, end=" ")
        print((i + 1) * "#")


# This is for, we can use functions different .py file without calling main all the time.
if __name__ == "__main__":
    # Add breakpoint here and look your codes with step into(f11) for debugging step by step.
    # Also you can add breakpoint where you want to add too.
    main()
