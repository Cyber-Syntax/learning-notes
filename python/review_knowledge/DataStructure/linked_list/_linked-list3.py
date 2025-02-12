"""Real life linked list example"""

class GameObject:
    def __init__(self, data):
        self.data = data
        self.next = None

class Game:
    def __init__(self):
        self.head = None

    def add_object(self, data):
        new_object = GameObject(data)
        if self.head is None:
            self.head = new_object
        else:
            current_object = self.head
            while current_object.next:
                current_object = current_object.next
            current_object.next = new_object

    def remove_object(self, position):
        new_object = self.head
        current_position = 0
        while new_object and current_position < position - 1:
            new_object = new_object.next
            current_position += 1

        if new_object is None:
            print("Position out of range")
            return

        if current_position == position - 1:
            self.head = new_object.next
        else:
            current_object.next = new_object.next

game = Game()
game.add_object("Character")
game.add_object("Item")
game.add_object("Enemy")

game.remove_object(1)

current_object = game.head
while current_object:
    print(current_object.data)
    current_object = current_object.next
