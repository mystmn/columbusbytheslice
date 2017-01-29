#!/usr/bin/env python
import os

#
# IMPORTANT: Put any additional includes below this line.  If placed above this
# line, it's possible required libraries won't be in your searchable path
#

from run import app as application

#
# Below for testing only
#
if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    httpd = make_server('localhost', 5002, application)
    # Wait for a single request, serve it and quit.
    httpd.serve_forever()
