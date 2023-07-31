#!/usr/bin/python3

"""
Setup flask application
"""
from api.v1.views import app_views
from flask import Flask, Blueprint
from models import storage
from os import getenv

app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def handle_teardown(obj):
    """Close the storage engine at the end of the request"""
    storage.close()


if __name__ == "__main__":
    """Set threaded=True, will tell Flask to use multiple
    threads to handle requests. This can improve performance, but
    it can also make it more difficult to debug problems.
    """
    app.run(
        debug=True, host=getenv('HBNB_API_HOST'),
        port=int(getenv('HBNB_API_PORT')), threaded=True
    )
