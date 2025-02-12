# Simple calculator with python

# operation functions
def sum(x, y):
    return x + y

def substract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

print("Select operation:")
print("1.Sum")
print("2.Substract(çıkarma)")
print("3.Multiply(çarpma)")
print("4.Divide(bölme)")

while True:
    # Take input from the user
    choice = input("Enter choice(1,2,3,4): ")

    # check if choice is one of the four options
    if choice in ("1", "2", "3", '4'):    
        # example: float = 2.0, int = 2       
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        

        if choice == "1":
            print(num1, "+", num2, "=", sum(num1, num2))
        elif choice == "2":
            print(num1, "-", num2, "=", sum(num1, num2))
        elif choice == "3":
            print(num1, "*", num2, "=", sum(num1, num2))
        elif choice == "4":
            print(num1, "/", num2, "=", sum(num1, num2))
        
        # check if user wants another calculation
        # break the wile loop if answer is no
        next_calculation = input("Let's do next calculation? (y/n): ")
        if next_calculation == "n":
            break
    else:
        print("Invalid input")
        break

