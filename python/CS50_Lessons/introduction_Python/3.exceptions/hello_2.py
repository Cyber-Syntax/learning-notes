def main():
    x = get_int("What's x:")
    print(f"x is {x}")

def get_int(prompt):
    while True:            
        try:  
            # We are using while we have to good reason to do that
            # It's up to apps or senior developers which one can be usable for which one apps
            return int(input(prompt)) 
            # x = int(input("x: "))
            # return x
        except ValueError:
            #print("x is not an integer")           
            # We can pass and reprompt to user
            pass      
            # I add this line to return new input to user can understand why we reprompt          
            while True:
                try:
                    return int(input("You need to write number for x: "))
                except ValueError:
                    pass
        #else:
            # Python can be return value like this
            # We don't need to use break because
            # We didn't want to increase lines of codes
            #return x        
            #break
    #return x

main()
    
