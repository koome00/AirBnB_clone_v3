#!/usr/bin/python3
'''
    flask with general routes
    routes:
        /status:    display "status":"OK"
        /stats:     dispaly total for all classes
'''
from api.v1.views import app_views
from flask import jsonify
from models import storage


@app_views.route("/status")
def status():
    '''
        return JSON of OK status
    '''
    return jsonify({'status': 'OK'})

@app_views.route('/stats')
def stats():
    """
    Creates and endpoint that retrieves the number of each objects by type
    """
    models = {'User': 'users', 'State': 'states',
              'Review': 'reviews', 'Place': 'places',
              'City': 'cities', 'Amenity': 'amenities'}

    objs = {}
    for key, value in models.items():
        objs[value] = storage.count(key)
    return jsonify(objs)
