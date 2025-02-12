# Write flask bookmark manager with sqlite, html and css
# We can add folders to folders like tree structure
# Bookmarks need to added folders
# We can delete, edit folders and bookmarks
 
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bookmarks.db'
db = SQLAlchemy(app)

# Folder model
class Folder(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False, unique=True)
    parent_id = db.Column(db.Integer)

# Bookmark model
class Bookmark(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False, unique=True)
    url = db.Column(db.String(300), nullable=False)
    folder_id = db.Column(db.Integer)

@app.route('/')
def index():
    folders = Folder.query.all()
    bookmarks = Bookmark.query.all()
    return render_template('index.html', folders=folders, bookmarks=bookmarks)

@app.route('/new_folder', methods=['POST'])
def new_folder():
    folder_name = request.form.get('folder_name')
    parent_id = request.form.get('parent_id')

    folder = Folder(name=folder_name, parent_id=parent_id)
    db.session.add(folder)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/edit_folder/<int:folder_id>', methods=['POST'])
def edit_folder(folder_id):
    folder = Folder.query.get(folder_id)
    folder.name = request.form.get('folder_name')
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/delete_folder/<int:folder_id>', methods=['POST'])
def delete_folder(folder_id):
    folder = Folder.query.get(folder_id)
    db.session.delete(folder)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/new_bookmark', methods=['POST'])
def new_bookmark():
    bookmark_name = request.form.get('bookmark_name')
    bookmark_url = request.form.get('bookmark_url')
    folder_id = request.form.get('folder_id')

    bookmark = Bookmark(name=bookmark_name, url=bookmark_url, folder_id=folder_id)
    db.session.add(bookmark)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/edit_bookmark/<int:bookmark_id>', methods=['POST'])
def edit_bookmark(bookmark_id):
    bookmark = Bookmark.query.get(bookmark_id)
    bookmark.name = request.form.get('bookmark_name')
    bookmark.url = request.form.get('bookmark_url')
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/delete_bookmark/<int:bookmark_id>', methods=['POST'])
def delete_bookmark(bookmark_id):
    bookmark = Bookmark.query.get(bookmark_id)
    db.session.delete(bookmark)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)