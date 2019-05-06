#!/usr/bin/python
from datetime import datetime
from json import dumps


def current_time():
    """Get current time to the second."""
    now = datetime.utcnow()
    format_date = now.strftime('%x %X')
    return dumps({'currentTime': format_date})
