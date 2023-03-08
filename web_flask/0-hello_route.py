#!/usr/bin/python3

"""# First flask route."""
from flask import Flask
from gevent.pywsgi import WSGIServer
app = Flask(__name__)


@app.route('/airbnb-onepage', strict_slashes=False)
def index():
    """# Display Hello HBNB."""
    return "Hello HBNB!"


if __name__ == "__main__":
    http_server = WSGIServer(('', 5000), app)
    http_server.serve_forever()
