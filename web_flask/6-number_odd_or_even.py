#!/usr/bin/python3

"""# using url parameter."""

from flask import Flask, abort, render_template

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


@app.route("/number/<n>", strict_slashes=False)
def num_route(n=0):
    """# return n is a number if a number."""
    try:
        num = int(n)
        return "{numb} is a number".format(numb=num)
    except (ValueError):
        return abort(404)


@app.route("/number_template/<n>", strict_slashes=False)
def num_template(n=0):
    """# render HTML page if it is a number."""
    try:
        num = int(n)
        return render_template('5-number.html', num=num)
    except (ValueError):
        return abort(404)


@app.route('/number_odd_or_even/<n>', strict_slashes=False)
def number_odd_or_even(n=0):
    """# Return even or odd."""
    try:
        num = int(n)
        show_even = "even"
        if num % 2 != 0:
            show_even = "odd"
        return render_template("6-number_odd_or_even.html", num=num, show_even=show_even)
    except (ValueError):
        return abort(404)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
