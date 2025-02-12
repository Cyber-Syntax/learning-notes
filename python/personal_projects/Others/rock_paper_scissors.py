# import modules
import random

# rock paper scissors
class Game:

    # get user input
    def get_input(self):
        hand = input("rock, paper, scissors? ")
        if hand != ["rock", "paper" "scissors"]:
            raise ValueError("Opps! You write wrong.")
        else:
            return hand
        
# random choice rock paper scissors
    def random(self):
    ... 
# get score when who win or say who win    

# rock kills scissors
# paper wraps rock.
# scissors cuts paper 

def main():
    get_input = Game().get_input()    
    print(get_input)

if __name__ == "__main__":
    main()