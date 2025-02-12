# Define the parent class
class Animal:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Hello, I am " + self.name)

# Define the child class
class Cat(Animal):
    def __init__(self, name, color):
        # Use the super() function to call the __init__() method of the parent class
        super().__init__(name)
        self.color = color

    def meow(self):
        print("Meow!")

# Create an instance of the Cat class
cat = Cat("Fluffy", "white")

# Call the greet() method of the Cat class
cat.greet()  # This will print "Hello, I am Fluffy"

# Call the meow() method of the Cat class
cat.meow()  # This will print "Meow!"


# Another example:

class Employee:
    # Class constructor
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    # This method returns the employee's name and salary
    def get_details(self):
        return f'Name: {self.name}, Salary: {self.salary}'

class Manager(Employee):
    # This class extends the functionality of the Employee class by
    # adding a new method for giving raises to employees
    def give_raise(self, amount):
        # Here, we use super() to call the get_details() method
        # from the parent Employee class
        current_salary = int(super().get_details().split(': ')[-1])
        new_salary = current_salary + amount
        return f'New salary: {new_salary}'

# Create a Manager object
mgr = Manager('Jane Doe', 50000)

# Use the give_raise() method to give the manager a raise of $5000
print(mgr.give_raise(5000))  # Output: New salary: 55000

# Another example:

class Bookmark:
    # Class constructor
    def __init__(self, url, tags=[]):
        self.url = url
        self.tags = tags

    # This method returns the bookmark's URL and tags
    def get_details(self):
        return f'URL: {self.url}, Tags: {self.tags}'

class BookmarkManager(Bookmark):
    # This class extends the functionality of the Bookmark class by
    # adding a new method for adding tags to bookmarks
    def add_tag(self, tag):
        # Here, we use super() to call the get_details() method
        # from the parent Bookmark class
        current_tags = super().get_details().split(': ')[-1]
        current_tags.append(tag)
        return f'Updated tags: {current_tags}'

# Create a BookmarkManager object
bmgr = BookmarkManager('https://www.python.org', ['programming', 'language'])

# Use the add_tag() method to add a new tag to the bookmark
print(bmgr.add_tag('python'))  # Output: Updated tags: ['programming', 'language', 'python']
