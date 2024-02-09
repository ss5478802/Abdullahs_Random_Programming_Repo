# Learning Flask microframework of Python
from flask import Flask, render_template
from markupsafe import escape

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("indexhtmlfileforflask.html")


@app.route("/<name>/")
def hello_world(name):
    return f"Hello {escape(name)}!"


@app.route("/<name>/<int:age>/")
@app.route("/<int:age>/<name>")
@app.route("/<int:age>/")
def age(age, name=None):
    if name != None:
        return f"Your name is {escape(name)} and ur age is {escape(age)}"
    else:
        return f"Your age is {escape(age)}"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
