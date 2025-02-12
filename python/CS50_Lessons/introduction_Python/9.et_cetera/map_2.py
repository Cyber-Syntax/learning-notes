def main():
    yell("This is YODA")

def yell(*words):
    # uppercased = []
    # for word in words:
    #     uppercased.append(word.upper())
    # print(*uppercased)

    uppercased = map(str.upper, words)
    print(*uppercased)


if __name__ == "__main__":
    main()