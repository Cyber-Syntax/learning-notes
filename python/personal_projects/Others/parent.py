# class Folders:
#     def __init__(self, name):
#         self.name = name
    
#     def printname(self):
#         print(self.name)

# class Bookmarks(Folders):
#     def __init__(self, name, title, url):                
#         super().__init__(name)
#         self.title = title
#         self.url = url
#         self.child_bookmarks = []

#     def add_child(self, child):
#         self.child_bookmarks.append(child)

#     def print_tree(self, indent=0):
#         print(' ' * indent + self.name)
#         print(' ' * indent + '  |')
#         print(' ' * indent + f'  |--> {self.title}')
#         print(' ' * indent + '         |')
#         print(' ' * indent + f'         |-> {self.url}')
#         for child in self.child_bookmarks:
#             child.print_tree(indent + 4)

# x = Bookmarks('Sites', 'github', 'github.com')
# y = Bookmarks('Sites', 'Google', 'google.com')
# x.add_child(y)
# x.print_tree()


class Folders:
    def __init__(self, name):
        self.name = name
    
    def printname(self):
        print(self.name)

class Bookmarks(Folders):
    def __init__(self, name, title, url, parent=None):                
        super().__init__(name)
        self.title = title
        self.url = url
        self.child_bookmarks = []
        self.parent = parent

    def add_child(self, child):
        self.child_bookmarks.append(child)

    def print_tree(self, indent=0):
        print(' ' * indent + self.name)
        print(' ' * indent + '  |')
        print(' ' * indent + f'  |--> {self.title}')
        print(' ' * indent + '         |')
        print(' ' * indent + f'         |-> {self.url}')
        for child in self.child_bookmarks:
            child.print_tree(indent + 4)
            if  >= 2 :
                print(' ' * indent + '  |')
                print(' ' * indent + f'  |--> {self.title}')
                print(' ' * indent + '         |')
                print(' ' * indent + f'         |-> {self.url}')    
                

# Create a Bookmarks object with a parent folder
folder = Folders('Sites')
x = Bookmarks('Sites', 'github', 'github.com', parent=folder)
y = Bookmarks('Sites', 'google', 'google.com', parent=folder)

# Print the tree to see the parent folder
x.print_tree()
y.print_tree()