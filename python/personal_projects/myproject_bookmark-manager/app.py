from flask import Flask, render_template, request, redirect
import sqlite3
from threading import Thread

app = Flask(__name__, template_folder="templates")

# function to get all bookmarks and folders from the database
def get_bookmarks():
    # create a connection to the database
    conn = sqlite3.connect("bookmarks.db")

    cur = conn.cursor()
    # execute a SQL query to select all bookmarks and folders from the database
    cur = conn.execute("SELECT id, parent_id, name, url FROM bookmarks")

    # loop through the results of the query
    for row in cur:
        id, parent_id, name, url = row

        # if the bookmark or folder doesn't have a parent, add it to the root of the bookmarks dictionary
        if parent_id is None:
            bookmarks[id] = {"name": name, "url": url, "children": {}}

        # if the bookmark or folder has a parent, add it to the children of the parent folder
        else:
            bookmarks[parent_id]["children"][id] = {"name": name, "url": url, "children": {}}
    
    # return the bookmarks dictionary
    return bookmarks


# route to display the bookmarks and folders
@app.route("/")
def index():
    conn = sqlite3.connect("bookmarks.db")
    # get the bookmarks from the database
    bookmarks = get_bookmarks()

    return render_template("index.html", bookmarks=bookmarks)

# route to add a new bookmark
@app.route("/add", methods=["POST"])
def add_bookmark():
    # get the bookmark URL and description from the form
    url = request.form["url"]
    description = request.form["description"]

    # insert the bookmark into the database
    conn.execute("INSERT INTO bookmarks (name, url) VALUES (?, ?)", (description, url))
    conn.commit()

    # get the bookmarks from the database
    bookmarks = get_bookmarks()

    return redirect(url_for("index"))

# route to add a new folder
@app.route("/addfolder", methods=["POST"])
def add_folder():
    # get the folder name and parent folder from the form
    name = request.form["name"]
    parent_folder = request.form["parent_folder"]

    # insert the folder into the database
    conn.execute("INSERT INTO bookmarks (name, parent_id) VALUES (?, ?)", (name, parent_folder))
    conn.commit()

    # get the bookmarks from the database
    bookmarks = get_bookmarks()

    return redirect(url_for("index"))

# route to move a bookmark to a folder
@app.route("/move", methods=["POST"])
def move_bookmark():
    # get the bookmark URL, the current folder it is in, and the destination folder from the form
    url = request.form["url"]
    current_folder = request.form["current_folder"]
    destination_folder = request.form["destination_folder"]

    # update the bookmark in the database
    conn.execute("UPDATE bookmarks SET parent_id = ? WHERE url = ?", (destination_folder, url))
    conn.commit()

    # get the bookmarks from the database
    bookmarks = get_bookmarks()

    return redirect(url_for("index"))

# route to delete a bookmark
@app.route("/delete/<id>", methods=["POST"])
def delete_bookmark(id):
    # delete the bookmark from the database
    conn.execute("DELETE FROM bookmarks WHERE id = ?", (id,))
    conn.commit()

    # get the bookmarks from the database
    bookmarks = get_bookmarks()

    return redirect(url_for("index"))

# route to delete a folder
@app.route("/deletefolder/<id>", methods=["POST"])
def delete_folder(id):
    # delete the folder and all its children from the database
    conn.execute("DELETE FROM bookmarks WHERE id = ? OR parent_id = ?", (id, id))
    conn.commit()

    # get the bookmarks from the database
    bookmarks = get_bookmarks()

    return redirect(url_for("index"))



if __name__ == "__main__":
    app.run()
