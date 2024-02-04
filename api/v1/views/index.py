#!/usr/bin/python3
""" index file """

from api.v1.views import app_views
from flask import jsonify
from models import storage

@app_views.route('/status', methods=['GET'])
def status():
    """ returns a JSON: "status": "OK" """
    response = {'status': 'OK'}
    return (jsonify(response))


@app_views.route('/stats', methods=['GET'])
def get_stats():
    """gets the no of each object by type"""
    stats = {
            'amenities': storage.count('Amenty'),
            'cities': storage.count('City'),
            'places': storage.count('Place'),
            'reviews': storage.count('Review'),
            'states': storage.count('State'),
            'users': storage.count('User')
            }
    return (jsonify(stats))
