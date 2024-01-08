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
from models import amenity, city, state, place, review, user

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
    objs  = {
        "amenities": storage.count(Amenity),
        "cities": storage.count(City),
        "places": storage.count(Place),
        "reviews": storage.count(Review),
        "states": storage.count(State),
        "users": storage.count(User)
        }
    
    return jsonify(objs)
