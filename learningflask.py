# Learning Flask microframework of Python
from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route("/")
def index():
    return """
    <!DOCTYPE html>
    <html>
    <head>
    <title>Abdullah's Flask Website!</title>
    </head>
    <body>
    <h1 style="color:red; text-align:center;">Welcome to Abdullah's Flask website!</h1>
    <h2 style = "color:blue; text-align:center;">To get ur name only displayed, type the address followed by a slash followed by ur name.</h2>
    <h3 style = "color:green;">For example: http://192.168.0.100:5000/John</h3>
    <h2 style = "color:blue; text-align:center;">To get ur age only displayed, type the address followed by a slash followed by ur age (in whole number, no decimal points.)</h2>
    <h3 style = "color:green;">For example: http://192.168.0.100:5000/30</h3>
    <h2 style = "color:blue; text-align:center;">To get ur name and age displayed, type the address followed by a slash followed by ur name/age followed by a slash followed by ur age/name.</h2>
    <h3 style = "color:green;">For example: http://192.168.0.100:5000/John/30 <br> OR <br> http://192.168.0.100:5000/30/John </h3>
    
    <h1 style = "text-align:center;">Enjoy using my website!</h1>
    </body>
    </html>"""


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
