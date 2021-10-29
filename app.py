from flask import Flask, render_template, request, redirect, url_for

db = {
    "todo": [{"description": 'Falseyoo', "title": 'yo'}],
    "doing": [{"description": 'Falseyoo', "title": 'yoo'}],
    "complete": [{"description": 'Falseyoo', "title": 'yooo'}]
}

app = Flask(__name__)


@app.route("/")
def index():
    print(db)
    return render_template('index.html', db=db)

@app.route("/add/<string:cat>", methods=["POST"])
def add(cat):
    title = request.form.get("title")
    description = request.form.get("description")
    db[cat].append({'title': title, 'description': description})
    return redirect(url_for("index"))

@app.route("/delete/<string:cat>/<int:pos>")
def delete(cat, pos):
    db[cat].pop(pos)
    return redirect(url_for("index"))

@app.route("/move/<string:initCat>/<int:pos>", methods=["POST"])
def move(initCat, pos):
    print('move was called')
    finalCat = request.form.get('finalCat')
    db[finalCat].append(db[initCat].pop(pos))
    return redirect(url_for("index"))

if (__name__ == "__main__"):
    app.run(debug=True)
