#!/usr/bin/env python3

from flask import (Blueprint, Response, current_app, request)
import random

app = current_app
siteapi = Blueprint('siteapi', __name__, url_prefix='/api')


@siteapi.route('/healthcheck')
def healthcheck():
    app.logger.info('healthcheck successfully pinged')
    return Response(status=204)


@siteapi.route('/resume')
def resume():
    app.logger.info('resume requested')
    with app.open_resource('static/resume.json') as resumefile:
        resume = resumefile.read()
    return Response(resume, status=200)


# curl -X POST localhost:5000/api/mockme -d '{"message": "why would you do this?"}' -H 'Content-Type: application/json'
@siteapi.route('/mockme', methods=['POST'])
def mockme():
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
