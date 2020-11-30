#!/usr/bin/env python3

import random

from flask import Blueprint, Response, current_app, request
from flask_swagger_ui import get_swaggerui_blueprint

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


@siteapi.route('/rolldice', methods=['GET'])
def rolldice():
    app.logger.info("Resource requested: " + request.url)
    rollednumber = 0
    dicenumber = int(request.args.get('dicenumber'))
    app.logger.debug('Number of dice in request: ' + str(dicenumber))
    dicesides = int(request.args.get('dicesides'))
    app.logger.debug('Number of sides on each die: ' + str(dicesides))
    for x in range(dicenumber):
        rollednumber += random.randint(1, dicesides)
    return str(rollednumber)
