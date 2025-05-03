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
        title = input("title: ").title()
        url = input("url: ")
        return (title, url)

bookmark_manager = BookmarkManager()

for i, bookmark in enumerate(bookmark_manager.get_bookmarks(), start=1):
    print(f"{i}. {bookmark}")

