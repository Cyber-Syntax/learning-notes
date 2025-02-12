import random

# We are doing this class because of the long codes need to understandable.
class Hat:

    houses = ["Gry", "Huffle", "Ravenclaw", "Sly"]

    @classmethod
    def sort(cls, name):
        print(name, "is in ", random.choice(cls.houses))

hat = Hat()
hat.sort("Harry")