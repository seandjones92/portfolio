#!/usr/bin/env python3

import os

import requests
from flask import (Blueprint, current_app, redirect, render_template, request,
                   url_for)

from .forms import mockingForm, rolldiceForm

if os.environ.get('FLASK_ENV') == 'development':
    resourcescheme = 'http'
else:
    resourcescheme = 'https'

app = current_app
sitegui = Blueprint('sitegui', __name__)


@sitegui.route('/')
def homepage():
    app.logger.info("Resource requested: " + request.url)
    projectfeedapi = url_for('siteapi.projectfeed',
                             _scheme=resourcescheme, _external=True)
    app.logger.debug('projectfeed api located at ' + projectfeedapi)
    projectfeed = requests.get(projectfeedapi).json()
    app.logger.debug('project feed content: ' + str(projectfeed))
    return render_template('home.html', projectfeed=projectfeed)


@sitegui.route('/about')
def about():
    app.logger.info("Resource requested: " + request.url)
    return render_template('about.html')


@sitegui.route('/mockme', methods=['GET', 'POST'])
def mockme():
    app.logger.info("Resource requested: " + request.url)
    form = mockingForm(request.form)
    userstextresponse = None

    mockmeapi = url_for(
        'siteapi.mockme', _scheme=resourcescheme, _external=True)

    app.logger.debug('Request method: ' + request.method)

    if request.method == 'POST':
        userstext = form.textToMockify.data
        userstextjson = {'message': userstext}
        userstextresponse = requests.post(mockmeapi, json=userstextjson).text
        app.logger.info("form posted successfully")

    if userstextresponse is None:
        form.textToMockify.data = ""
    else:
        form.textToMockify.data = userstextresponse

    return render_template('mockme.html', mockedtext=userstextresponse, form=form)


@sitegui.route('/rolldice')
def rolldice():
    app.logger.info("Resource requested: " + request.url)
    form = rolldiceForm(request.form)

    rolldiceapi = url_for('siteapi.rolldice',
                          _scheme=resourcescheme, _external=True)

    dicenumber = request.args.get('dicenumber')
    if dicenumber == None:
        dicenumber = 0
    app.logger.debug('Number of dice to roll: ' + str(dicenumber))

    dicesides = request.args.get('dicesides')
    if dicesides == None:
        dicesides = 0
    app.logger.debug('Number of dice to roll: ' + str(dicesides))

    params = {'dicenumber': dicenumber, 'dicesides': dicesides}
    rollednumber = requests.get(rolldiceapi, params=params).text
    app.logger.debug('Rolled number is: ' + str(rollednumber))

    form.dicenumber.data = dicenumber
    form.dicesides.data = dicesides

    return render_template('rolldice.html', form=form, rollednumber=rollednumber)
