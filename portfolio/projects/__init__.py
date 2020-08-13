#!/usr/bin/env python3

from flask import (Blueprint, request, url_for, render_template)
from wtforms import (Form, StringField)
import requests

siteprojects = Blueprint('siteprojects', __name__, url_prefix='/projects')


class mockingForm(Form):
    textToMockify = StringField('Your text here')


@siteprojects.route('/mockme', methods=['GET', 'POST'])
def mockmefrontend():
    form = mockingForm(request.form)
    mockmeapi = url_for('siteapi.mockme', _scheme='https', _external=True)
    userstextresponse = ""
    if request.method == 'POST':
        userstext = form.textToMockify.data
        userstextjson = {'message': userstext}
        userstextresponse = requests.post(mockmeapi, json=userstextjson).text
    pagecontent = {'mockedtext': userstextresponse}
    return render_template('mockme.html', pagecontent=pagecontent, form=form)
