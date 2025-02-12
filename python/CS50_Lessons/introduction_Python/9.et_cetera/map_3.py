def main():
    yell("This is YODA")

def yell(*words):
    #uppercased = map(str.upper, words)
    #python list comprehension
    uppercased = [word.upper() for word in words]
    print(*uppercased)


if __name__ == "__main__":
    main()