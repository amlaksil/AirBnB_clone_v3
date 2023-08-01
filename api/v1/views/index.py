#!/usr/bin/python3
"""Create route"""
from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """Returns Json object"""
    return jsonify({"status": "OK"})

'''
@app_views.route('/stats', methods=['GET'], strict_slashes=False)
def stats():
	"""Returns the number of instance """
	return jsonify(jsonify(amenities=storage.count("Amenity"),
                   cities=storage.count("City"),
                   places=storage.count("Place"),
                   reviews=storage.count("Review"),
                   states=storage.count("State"),
users=storage.count("User")))
'''
