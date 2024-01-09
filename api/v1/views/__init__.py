#!/usr/bin/python3
""" Init defintion for views package"""
from flask import Blueprint


app_views = Blueprint("app_views", __name__, url_prefix="/api/v1")

from api.v1.views.index import *

from api.v1.views.states import *
from api.v1.views.cities import *
<<<<<<< HEAD
from api.v1.views.users import *
=======
from api.v1.views.amenities import *
>>>>>>> 5d8a88df13903cac7759b34b231d55b87da88b0a
