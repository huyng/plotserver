from flask import Flask, make_response
from StringIO import StringIO

def show(context, path="/", host="127.0.0.1", port=8080):
    """
    Arguments:

    context - A matplotlib Figure or pylab environment
    path    - Url path to serve your matplotlib figure
    host    - host address to bind http server to (default: 127.0.0.1)
    port    - host port to bind http server to (default: 8080)
    """

    newapp = Flask(__name__)
    @newapp.route(path)
    def dynamic():
        buf = StringIO()
        context.savefig(buf, format='png')
        buf.seek(0)
        response = make_response(buf.read())
        response.headers['Content-Type'] = 'image/png'
        return response

    newapp.run(port=port, host=host)