# When we add module with "from random" , we don't need to add random.choice. 
# We can use just choise[..]

# import modules
from random import choice, randint, shuffle

# heads and tails defining list
# It's randomly printing this list values
coin = choice(["heads", "tails(kuyruk)"])

# Generate random numbers from 1 to 4
number = randint(1, 4)

# shuffling(karıştır)
cards = ["Yoda", "Obiricks", "Jack"]
shuffle(cards)
for card in cards:
    print(card)
print("\n")
print(number)
print(coin)