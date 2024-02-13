# Learning Flask microframework of Python
from flask import Flask, request, render_template, redirect, url_for
from markupsafe import escape
from random import choice

app = Flask(__name__)
colours_for_other_tags = [
    "aqua",
    "black",
    "blue",
    "fuchsia",
    "gray",
    "green",
    "lime",
    "maroon",
    "navy",
    "olive",
    "purple",
    "red",
    "teal",
    "yellow",
]
colours_for_background = [
    "white",
    "ivory",
    "lightblue",
    "paleyellow",
    "gainsboro",
    "powderblue",
    "lightyellow",
    "peachpuff",
    "lavender",
    "antiquewhite",
]


@app.route("/")
def index():
    return render_template("indexhtmlfileforflask.html")


@app.route("/", methods=["POST"])
def process_form():
    name = request.form.get("name")
    age = request.form.get("age")
    if name and age:
        return redirect(url_for("age", age=age, name=name.title()))
    elif name:
        return redirect(url_for("hello_world", name=name.title()))
    elif age:
        return redirect(url_for("age", age=age))
    else:
        return redirect(url_for("index"))


@app.route("/<name>/")
def hello_world(name):
    if name.strip() != "":
        return render_template(
            "helloWorld.html",
            persons_name=name,
            heading_colour=choice(colours_for_other_tags),
            bgcolour=choice(colours_for_background),
        )
    else:
        return (
            "<h1 style='color:red;'>Name is missing. Enter your name in the URL!</h1>"
        )


@app.route("/<name>/<int:age>/")
@app.route("/<int:age>/<name>/")
@app.route("/<int:age>/")
def age(age, name=None):
    return render_template(
        "age.html",
        persons_name=name,
        persons_age=age,
        heading_colour=choice(colours_for_other_tags),
        bgcolour=choice(colours_for_background),
    )


@app.errorhandler(404)
def error_page(e):
    return render_template("404error.html", error=str(e)[19:])


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
