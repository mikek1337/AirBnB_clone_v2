#!/usr/bin/python3

"""# using url parameter."""

from flask import Flask, abort

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    """# index route."""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """# hbnb route."""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    """# C route."""
    text = str(text)
    text = text.split("_")
    text = " ".join(text)
    return "C " + text


@app.route("/python/", defaults={'text': 'is cool'})
@app.route("/python/<text>", strict_slashes=False)
def python_text(text="is cool"):
    """# Python route."""
    text = str(text)
    text = text.split("_")
    text = " ".join(text)
    return "Python " + text


@app.route("/number/<n>")
def num_route(n=0):
    """# return n is a number if a number."""
    try:
        num = int(n)
        return "{numb} is a number".format(numb=num)
    except (ValueError):
        return abort(404)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
