#!/usr/bin/env python3

from flask import (Blueprint, Response, current_app)

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
