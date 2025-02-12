# Our modules

def main():
    hello("world")
    goodbye("world")

def hello(name):
    print(f"hello, {name}")

def goodbye(name):
    print(f"goodbye, {name}")

# It's allow us to use functions in other python file with module system.
if __name__ == "__main__":
    main()

