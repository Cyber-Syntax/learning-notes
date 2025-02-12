import sqlite3
from flask import Flask, render_template

# Create a new Flask app
app = Flask(__name__)

# Define a route for the homepage
@app.route("/")
def home():
  # Connect to the database
  conn = sqlite3.connect("bookmarks.db")
  cur = conn.cursor()

  # Get all bookmarks from the database
  cur.execute("SELECT id, parent_id, name, url FROM bookmarks")
  bookmarks = cur.fetchall()

  # Close the database connection
  cur.close()
  conn.close()

  # Render the HTML template, passing the bookmarks data to it
  return render_template("bookmarks.html", bookmarks=bookmarks)

# Run the app
if __name__ == "__main__":
  app.run()
