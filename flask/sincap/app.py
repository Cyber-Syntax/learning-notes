from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bookmarks.db'
db = SQLAlchemy(app)
    

class Bookmark(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(200))
    description = db.Column(db.String(300))

db.create_all()

@app.route('/')
def index():
    bookmarks = Bookmark.query.all()
    return render_template('index.html', bookmarks=bookmarks)

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        url = request.form['url']
        description = request.form['description']
        bookmark = Bookmark(url=url, description=description)
        db.session.add(bookmark)
        db.session.commit()
        return redirect('/')
    return render_template('add.html')

if __name__ == '__main__':
    app.run()
