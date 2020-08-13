#!/usr/bin/env python3

from flask import (Blueprint, Response, current_app, request, redirect)
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
    with app.open_resource('static/assets/json/resume.json') as resumefile:
        resume = resumefile.read()
    return Response(resume, status=200)


@siteapi.route('/mockme', methods=['POST'])
def mockme():
    response = handle_proxy_http_to_https()
    if response is not None:
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


@siteapi.route('/emacs', methods=['GET'])
def emacsinstaller():
    isprivate = request.args.get('private')
    if isprivate == 'true':
        with app.open_resource(
                'static/assets/scripts/emacsprivate.sh') as emacsfile:
            emacsscript = emacsfile.read()
    else:
        with app.open_resource(
                'static/assets/scripts/emacspublic.sh') as emacsfile:
            emacsscript = emacsfile.read()
    return Response(emacsscript, status=200)


def handle_proxy_http_to_https():
    host = request.host
    if ':' in host:
        host = host.split(':')[0]
    if host != 'localhost':
        for i in request.headers:
            if i[0].lower() == 'x-forwarded-proto':
                if i[1].lower() == 'http':
                    url = 'https://' + host + request.path
                    response = redirect(url, 308)
                    return response
    return None
