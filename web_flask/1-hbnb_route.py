#!/usr/bin/python3

"""# adding additional route."""

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    """# index of the page."""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """# route to hbnb."""
    return "HBNB"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
