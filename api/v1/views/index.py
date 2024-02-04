#!/usr/bin/python3
""" index file """

from api.v1.views import app_views
import jsonify

@app_views.route('/status')
def status():
    """ returns a JSON: "status": "OK" """
    return (jsonify({'status': 'OK'}), 200)
