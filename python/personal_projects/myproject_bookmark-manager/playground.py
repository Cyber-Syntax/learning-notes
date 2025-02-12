from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

# Connect to the database
conn = sqlite3.connect('bookmarks.db', check_same_thread=False)

# Create the table
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS bookmarks(id integer primary key, name text, url text)''')

# Render the HTML homepage
@app.route("/")
def index():
    # Fetch the bookmarks from the database
    c = conn.cursor()
    c.execute("SELECT * FROM bookmarks")
    bookmarks = c.fetchall()
    return render_template("index.html", bookmarks=bookmarks)

# Add a new bookmark
@app.route("/add", methods=["POST"])
def add():
    # Get the form data
    name = request.form.get("name")
    url = request.form.get("url")

    # Insert the data into the database
    c = conn.cursor
    # keep going
    c.execute("INSERT INTO bookmarks (name, url) VALUES (?, ?)", (name, url))
    conn.commit()

    # Redirect to the homepage
    return redirect("/")

# Edit a bookmark
@app.route("/edit/<int:id>")
def edit(id):
    # Fetch the bookmark from the database
    c = conn.cursor()
    c.execute("SELECT * FROM bookmarks WHERE id=?", (id,))
    bookmark = c.fetchone()
    return render_template("edit.html", bookmark=bookmark)

# Update the database with the edited bookmark
@app.route("/update/<int:id>", methods=["POST"])
def update(id):
    # Get the form data
    name = request.form.get("name")
    url = request.form.get("url")
    
    # Update the database
    c = conn.cursor()
    c.execute("UPDATE bookmarks SET name=?, url=? WHERE id=?", (name, url, id))
    conn.commit()
 # keep going

# Delete a bookmark
@app.route("/delete/<int:id>")
def delete(id):
    # Delete the bookmark from the database
    c = conn.cursor()
    c.execute("DELETE FROM bookmarks WHERE id=?", (id,))
    conn.commit()

    # Redirect to the homepage
    return redirect("/")

# Run the application
if __name__ == '__main__':
    app.run(debug=True)