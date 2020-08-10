#!/usr/bin/env python3

import flask
from flask import (Blueprint, render_template)
import requests

sitegui = Blueprint('sitegui', __name__)


@sitegui.route('/')
def homepage():
    resumeapi = flask.request.host_url + "/api/resume"
    resumejs = requests.get(resumeapi)
    return render_template('index.html', resume=resumejs.json())
