#!/usr/bin/env python3

from flask import (Blueprint, current_app, request, url_for, render_template,
                   redirect)
from wtforms import (Form, StringField)
import requests

app = current_app
sitegui = Blueprint('sitegui', __name__)


@sitegui.route('/')
def homepage():
    app.logger.info("Resource requested: " + request.url)
    projectfeedapi = url_for('siteapi.projectfeed', _scheme='https', _external=True)
    # projectfeedapi = url_for('siteapi.projectfeed', _scheme='http', _external=True)
    projectfeed = requests.get(projectfeedapi).json()
    return render_template('home.html', projectfeed=projectfeed)


@sitegui.route('/about')
def about():
    app.logger.info("Resource requested: " + request.url)
    return render_template('about.html')


class mockingForm(Form):
    textToMockify = StringField('Your text here')


@sitegui.route('/mockme', methods=['GET', 'POST'])
def mockme():
    app.logger.info("Resource requested: " + request.url)
    form = mockingForm(request.form)
    userstextresponse = None

    # Uncomment this line for running in prod behind certs #
    mockmeapi = url_for('siteapi.mockme', _scheme='https', _external=True)
    # Uncomment this line for running locally without certs #
    # mockmeapi = url_for('siteapi.mockme', _scheme='http', _external=True)

    if request.method == 'POST':
        userstext = form.textToMockify.data
        userstextjson = {'message': userstext}
        userstextresponse = requests.post(mockmeapi, json=userstextjson).text
        app.logger.info("POST Successful")

    if userstextresponse is None:
        form.textToMockify.data = ""
    else:
        form.textToMockify.data = userstextresponse

    return render_template('mockme.html', mockedtext=userstextresponse, form=form)


@sitegui.route('/rolldice')
def rolldice():
    app.logger.info("Resource requested: " + request.url)
    return render_template('rolldice.html')
