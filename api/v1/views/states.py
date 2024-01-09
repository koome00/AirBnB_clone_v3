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
from models.state import State


@app_views.route("/states", methods=['Get'], strict_slashes=False)
def get_states():
    """
    get states object
    """
    states = []
    for objs in storage.all(State).values():
        states.append(objs.to_dict())
    return jsonify(states)


@app_views.route("/states/<state_id>", methods=['GET'], strict_slashes=False)
def get_states_using_id(state_id):
    """
    get state objects given state_id
    """
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    return jsonify(state.to_dict())


@app_views.route("/states", methods=['POST'], strict_slashes=False)
def create_states():
    """
    post method for states
    """
    if request.json is None:
        return "Not a JSON", 400
    fields = request.json
    if fields.get('name') is None:
        return "Missing name", 400
    new_state = State(**fields)
    new_state.save()
    return make_response(jsonify(new_state.to_dict()), 201)


@app_views.route("/state/<state_id>", methods=["PUT"], strict_slashes=False)
def update_states_with_id(state_id):
    """
    update state object
    """
    if request.json is None:
        return "Not a JSON", 400
    fields = request.get_json()
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    for key, value in fields.items():
        if key not in ['id', 'updated_at', 'created_at']:
            if hasattr(state, key):
                setattr(state, key, value)
    state.save()
    return make_response(jsonify(state.to_dict()), 200)


@app_views.route("/state/<state_id>", methods=['DELETE'], strict_slashes=False)
def delete_state(state_id):
    """
    deletes state objects when given id
    """
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    storage.delete(state)
    storage.save()
    return jsonify({}), 200
