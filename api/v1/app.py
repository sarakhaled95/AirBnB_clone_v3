#!/usr/bin/python3
"""create a variable app, instance of Flask
import storage from models
import app_views from api.v1.views
register the blueprint app_views to your Flask instance app
declare a method to handle @app.teardown_appcontext"""
from models import storage
from api.v1.views import app_views
from flask import Flask, make_response, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app, resources={r'/api/v1/*': {"origins": "0.0.0.0"}})
app.register_blueprint(app_views)
app.url_map.strict_slashes = False
HBNB_API_HOST = os.getenv("HBNB_API_HOST")
HBNB_API_PORT = os.getenv("HBNB_API_PORT")


@app.teardown_appcontext
def teardown_db(exception):
    """ teardown: declare a method to handle @app.teardown_appcontext that
        calls storage.close()"""
    storage.close()


@app.errorhandler(404)
def found_not(error):
    """ 404 not found error """
    return (make_response(jsonify({'error': 'Not found'}), 404))


if __name__ == "__main__":
    if not HBNB_API_HOST:
        HBNB_API_HOST = "0.0.0.0"
    if not HBNB_API_PORT:
        HBNB_API_PORT = "5000"
    app.run(host=HBNB_API_HOST, port=HBNB_API_PORT, threaded=True)
