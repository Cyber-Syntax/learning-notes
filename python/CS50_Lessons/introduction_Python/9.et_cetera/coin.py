def main():
    n = int(input("n: "))
    #for i in range(n):
        #print("coin" * i )
        #print(coin(i))
    for s in coin(n):
        print(s)

def coin(n):
    #return "🪙" * n
    
    # Ram struggle with this code when you use this    
    """
    flock = []
    for i in range(n):
        flock.append("🪙" * i )
    return flock
    """

    # yield can be solve this problem
    for i in range(n):
        # yield
        yield "🪙" * i

        # It's not gonna give you when you use 100000 value, It's gonna return 0
        """
        return "🪙" * i
        """
        
       




if __name__ == "__main__":
    main()