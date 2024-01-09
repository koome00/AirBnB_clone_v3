#!/usr/bin/python3
"""
View for State objects that handles all default RESTFul API actions:
    GET
    GET (state_id)
    POST
    PUT
    DELETE
"""
from api.v1.views import app_views
from flask import jsonify, abort, make_response, request
from models import storage
from models.amenity import Amenity


@app_views.route("/amenities", methods=['GET'], strict_slashes=False)
def get_amenities():
    """
    retrieve all amenities obj
    """
    amenities = []
    for objs in storage.all(Amenity).values():
        amenities.append(objs.to_dict())
    return jsonify(amenities)


@app_views.route("amenities/<amenity_id>", methods=['GET'],
                 strict_slashes=False)
def get_amenities_id(amenity_id):
    """
    retrieve amenity object given id
    """
    amenity = storage.get(Amenity, amenity_id)
    if amenity is None:
        abort(404)
    return jsonify(amenity.to_dict())


@app_views.route("amenities/<amenity_id>", methods=['DELETE'],
                 strict_slashes=False)
def delete_obj(amenity_id):
    """"
    delete amenity obj given amenity id
    """
    amenity = storage.get(Amenity, amenity_id)
    if amenity is None:
        abort(404)
    storage.delete(amenity)
    storage.save()
    return jsonify({}), 200


@app_views.route("/amenities", methods=['POST'], strict_slashes=False)
def create_new():
    """"
    create new amenity object
    """
    if not request.get_json():
        return jsonify({'error': 'Not a JSON'}), 400
    fields = request.get_json()
    if 'name' not in fields:
        return jsonify({'error': 'Missing name'}), 400
    new_amenity = Amenity(**fields)
    new_amenity.save()
    return jsonify(new_amenity.to_dict()), 201


@app_views.route('/amenities/<amenities_id>',
                 methods=['PUT'], strict_slashes=False)
def update_amenity(amenities_id):
    '''
        update existing amenity object
    '''
    if not request.get_json():
        return jsonify({"error": "Not a JSON"}), 400
    obj = storage.get(Amenity, amenities_id)
    if obj is None:
        abort(404)
    obj_data = request.get_json()
    obj.name = obj_data['name']
    obj.save()
    return jsonify(obj.to_dict()), 200
