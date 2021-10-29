from flask import Flask, render_template, request, redirect, url_for

"""
Dictionary db acting as database containing tasks for the different categories
Every individual task has a name and a description
"""
db = {
    "todo": [],
    "doing": [],
    "complete": []
}

# initializing Flask
app = Flask(__name__)


@app.route("/")  # Index page function
def index():
    return render_template('index.html', db=db)


# Function to handle adding tasks
@app.route("/add/<string:cat>", methods=["POST"])
def add(cat):
    # Getting the title and description from the request as they were entered in the form
    title = request.form.get("title")
    description = request.form.get("description")
    db[cat].append({'title': title, 'description': description})
    # Redirecting so the page refreshes with the new data
    return redirect(url_for("index"))


# Function to handle deleting tasks
@app.route("/delete/<string:cat>/<int:pos>")
def delete(cat, pos):
    db[cat].pop(pos)
    return redirect(url_for("index"))


# Function to transfer tasks between categories
@app.route("/move/<string:initCat>/<int:pos>", methods=["POST"])
def move(initCat, pos):
    # Getting the final category from the dropdown
    finalCat = request.form.get('finalCat')
    # Popping from the initial category and inserting into the final category
    db[finalCat].append(db[initCat].pop(pos))
    return redirect(url_for("index"))


if (__name__ == "__main__"):
    app.run(debug=True)
