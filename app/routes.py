from app import app
from app import skyfield_service
from flask import request
import json

@app.route('/')
def root():
    return "Welcome to Skyfield JSON API. For more information, reference https://github.com/Matt-Weiss/skyfield_json and https://rhodesmill.org/skyfield/"

@app.route('/ephemerides')
def ephemerides():
    latitude = str(request.args.get('latitude')).replace("_", " ").upper()
    longitude = str(request.args.get('longitude')).replace("_", " ").upper()
    celestial_bodies = request.args.get('bodies').split(',')

    result = skyfield_service.SkyfieldService.ephemerides(latitude, longitude, celestial_bodies)

    return json.dumps(result)

@app.route('/telescope_tracking')
def telescope_tracking():
    latitude = str(request.args.get('latitude')).replace("_", " ").upper()
    longitude = str(request.args.get('longitude')).replace("_", " ").upper()
    celestial_body = str(request.args.get('body'))

    result = skyfield_service.SkyfieldService.telescope_tracking(latitude, longitude, celestial_body)

    return json.dumps(result)
