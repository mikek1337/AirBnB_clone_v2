#!/usr/bin/python3

"""Display states."""

from models import storage
from flask import Flask, render_template, abort

app = Flask(__name__)


@app.teardown_appcontext
def teardown():
    """Deserilize all."""
    storage.close()


@app.route("/states_list", strict_slashes=False)
def index():
    """Index page."""
    states = storage.all()
    print(states)
    return states


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
