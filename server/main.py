#!/usr/bin/python
"""Main time server application."""

from flask import Flask


try:
    # Running locally as module
    from server.util import clock
except ModuleNotFoundError:  # pragma: no cover
    # Running as a script
    from util import clock

app = Flask(__name__)


@app.route('/')
def main():
    """Return current system time."""
    return clock.current_time()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)  # pragma: no cover
