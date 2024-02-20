# Learning Flask microframework of Python
from flask import Flask, request, render_template, redirect, url_for
from random import choice
import re
import requests
from jokesapi import jokesapi
from apscheduler.schedulers.background import BackgroundScheduler

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


def jokes():
    jokehtml = requests.get(
        "https://api.api-ninjas.com/v1/jokes", headers={"X-Api-Key": jokesapi()}
    )
    with open("joke.txt", "w") as f:
        f.write(jokehtml.json()[0]["joke"])


schedule = BackgroundScheduler()
schedule.add_job(jokes, "interval", days=1)
schedule.start()


@app.route("/")
def index():
    with open("joke.txt", "r") as f:
        joke = f.read()
    return render_template("indexhtmlfileforflask.html", jokehtml=joke)


@app.route("/", methods=["POST"])
def process_form():
    name = request.form.get("name")
    age = request.form.get("age")
    if name.strip() != "" and age:
        return redirect(url_for("age", age=age, name=name.title()))
    elif name.strip() != "":
        return redirect(url_for("hello_world", name=name.title()))
    elif age:
        return redirect(url_for("age", age=age))
    else:
        return redirect(url_for("index"))


@app.route("/<name>/")
def hello_world(name):
    pattern = "^[a-zA-z -]*$"
    if name.strip() != "" and re.match(pattern, name):
        return render_template("helloWorld.html", persons_name=name)
    else:
        return render_template("errorhelloWorld.html")


@app.route("/<name>/<int:age>/")
@app.route("/<int:age>/<name>/")
@app.route("/<int:age>/")
def age(age, name=None):
    return render_template(
        "age.html",
        persons_name=name.title() if name else name,
        persons_age=age,
        heading_colour=choice(colours_for_other_tags),
        bgcolour=choice(colours_for_background),
    )


@app.errorhandler(404)
def error_page(e):
    return render_template("404error.html", error=str(e)[19:])


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
