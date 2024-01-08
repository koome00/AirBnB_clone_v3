#!/usr/bin/python3
""" Module containing views """
from api.v1.views import app_views
from flask import jsonify
from models import storage


@app_views.route("/status", strict_slashes=False)
def status():
    """ returns a JSON """
    status = {"status": "OK"}
    return jsonify(status)
