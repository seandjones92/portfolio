#!/usr/bin/env python3

from flask import (Blueprint, Response, current_app, request)
from flask_swagger_ui import get_swaggerui_blueprint
import random

swaggerurl = '/api-docs'
apiurl = '/static/assets/json/swagger.json'
swaggerblueprint = get_swaggerui_blueprint(swaggerurl,
                                           apiurl,
                                           config={'app_name': 'My APIs'})

app = current_app
siteapi = Blueprint('siteapi', __name__, url_prefix='/api')


@siteapi.route('/healthcheck')
def healthcheck():
    app.logger.info("Resource requested: " + request.url)
    return Response(status=204)


@siteapi.route('/projectfeed')
def projectfeed():
    app.logger.info("Resource requested: " + request.url)
    return app.send_static_file('assets/json/projectfeed.json')


@siteapi.route('/mockme', methods=['POST'])
def mockme():
    app.logger.info("Resource requested: " + request.url)
    output_text = ""
    input_text = str(request.json.get('message'))
    for char in input_text:
        if char.isalpha():
            if random.random() > 0.5:
                output_text += char.upper()
            else:
                output_text += char.lower()
        else:
            output_text += char
    return output_text


@siteapi.route('/roll', methods=['POST'])
def diceroll():
    app.logger.info("Resource requested: " + request.url)
    rollednumber = 0
    dicenumber = int(request.json.get('dicenumber'))
    dicesides = int(request.json.get('dicesides'))
    rollmodifier = int(request.json.get('rollmodifier'))
    for x in range(dicenumber):
        rollednumber += random.randint(0, dicesides)
    rolltotal = rollednumber + rollmodifier
    rollresults = {
        "diceNumber": dicenumber,
        "diceSides": dicesides,
        "rollModifier": rollmodifier,
        "rolledNumber": rollednumber,
        "rollTotal": rolltotal
    }
    return rollresults
