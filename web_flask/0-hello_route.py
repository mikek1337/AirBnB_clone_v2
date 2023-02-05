#!/usr/bin/python3

"""First flask route."""
from web_flask import app

@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Display Hello HBNB."""
    return "Hello HBNB!"
