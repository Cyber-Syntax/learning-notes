# Defined main code to work in this code in specific space
def main():
    x = -3
    if is_even(x):
        print("Even")
    else:
        print("Odd")

# Defining function for is number even or odd?
def is_even(n):
    return True if n % 2 == 0 else False
    
    # Other option to use this code
    # if n % 2 == 0:
    #     return True
    # else:
    #     # boolean True and False and they need to be capital(baş harfleri büyük)
    #     return False
main()