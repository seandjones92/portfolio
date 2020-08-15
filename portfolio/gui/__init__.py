#!/usr/bin/env python3

from flask import Blueprint

sitegui = Blueprint('sitegui', __name__)


@sitegui.route('/')
def homepage():
    return "Working on it..."
