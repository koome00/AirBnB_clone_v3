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
    ams =[]
    if place is None:
        abort(404)
    else:
        for k in place.amenities:
            ams.append(k.to_dict())
        return jsonify(ams)


@app_views.route("/places/<place_id>/amenities/<amenity_id>",
                 methods=['DELETE'], strict_slashes=False)
def delete_amenity(place_id, amenity_id):
    place = storage.all(Place, place_id)
    amenity = storage.all(Amenity, amenity_id)

    if place is None or amenity is None:
        abort(404)
    if amenity not in place.amenities:
        abort(404)
    place.amenities.delete(amenity)
    place.save()

    return jsonify({}), 200
