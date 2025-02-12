import sqlite3

# create a connection to the database
conn = sqlite3.connect("bookmarks.db")

# create a table to store our bookmarks and folders
conn.execute("""
    CREATE TABLE bookmarks (
        id INTEGER PRIMARY KEY,
        parent_id INTEGER,
        name TEXT,
        url TEXT
    );
""")
