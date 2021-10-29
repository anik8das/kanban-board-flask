from flask import Flask, render_template

db = {
    "todo": [{"id": 1, "description": 'Falseyoo', "title": 'yo'}],
    "doing": [{"id": 1, "description": 'Falseyoo', "title": 'yoo'}],
    "complete": [{"id": 1, "description": 'Falseyoo', "title": 'yooo'}]
}

app = Flask(__name__)


@app.route("/")
def index():
    print(db)
    return render_template('index.html', db=db)


@app.route("/add")
def add():
    return "<p>Hello, Index!</p>"


if (__name__ == "__main__"):
    app.run(debug=True)
