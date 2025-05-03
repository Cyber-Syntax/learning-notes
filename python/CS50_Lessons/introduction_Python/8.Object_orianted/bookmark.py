class Bookmark:
    def __init__(self, title, url):
        self.title = title
        self.url = url

    def __str__(self):
        return f"{self.title} ({self.url})"

class BookmarkManager:
    def __init__(self):
        self.bookmarks = []

    def add_bookmark(self, bookmark):
        self.bookmarks.append(bookmark)

    def remove_bookmark(self, bookmark):
        self.bookmarks.remove(bookmark)

    def get_bookmarks(self):
        return self.bookmarks

# Create a BookmarkManager object
bm_manager = BookmarkManager()

# Create some Bookmark objects
bookmark1 = Bookmark("Python official site", "https://www.python.org/")
bookmark2 = Bookmark("Python documentation", "https://docs.python.org/3/")
bookmark3 = Bookmark("Python tutorials", "https://docs.python.org/3/tutorial/")

# Add the bookmarks to the manager
bm_manager.add_bookmark(bookmark1)
bm_manager.add_bookmark(bookmark2)
bm_manager.add_bookmark(bookmark3)

# Print the bookmarks
for bookmark in bm_manager.get_bookmarks():
    print("\n", bookmark)

print("\n")

# Remove a bookmark
bm_manager.remove_bookmark(bookmark2)

# Print the bookmarks again
for bookmark in bm_manager.get_bookmarks():
    print(bookmark)
