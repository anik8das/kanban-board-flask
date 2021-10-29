from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

toDo = []
doing = []
complete = []

app = Flask(__name__)


@app.route("/")
def index():
    print(toDo)
    return render_template('index.html', todo_list=[{"id": 1, "complete": 'no', "title": 'yo'}])


@app.route("/add")
def add():
    return "<p>Hello, Index!</p>"


if (__name__ == "__main__"):
    app.run(debug=True)
