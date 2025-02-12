def main():
    name = input("What's your name: ").title()
    hello(name)


def hello(to = "world"):
    print("Hello, " + to)
    #return f"hello, {to}"

if __name__ == "__main__":
    main()
