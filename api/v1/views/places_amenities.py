#!/usr/bin/python3
""" Module containing Review View """
from api.v1.views import app_views
from models.place import Place
from models.amenity import Amenity
from flask import Flask, jsonify, abort, request
from models import storage


@app_views.route("/places/<place_id>/amenities", methods=['GET'],
                 strict_slashes=False)
def get_amenity(place_id):
    """
    Retrieves the list of all Amenity objects of a Place
    """
    place = storage.get(Place, place_id)
    ams = []
    if place is None:
        abort(404)
    else:
        for k in place.amenities:
            ams.append(k.to_dict())
        return jsonify(ams)
