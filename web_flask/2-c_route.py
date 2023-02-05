#!/usr/bin/python3

"""# using url parameter."""

from flask import Flask

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


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
