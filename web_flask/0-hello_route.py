#!/usr/bin/python3

"""First flask route."""
from web_flask import app


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Display Hello HBNB."""
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
