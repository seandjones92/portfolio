#!/usr/bin/env python3

from flask import Flask
from flask_swagger_ui import get_swaggerui_blueprint
from portfolio import api, gui
import logging

SWAGGER_URL = '/api-docs'
API_URL = '/static/assets/json/swagger.json'
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(SWAGGER_URL,
                                              API_URL,
                                              config={'app_name': 'My APIs'})


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.register_blueprint(api.siteapi)
    app.register_blueprint(gui.sitegui)
    app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)

    return app


app = create_app()

if __name__ != '__main__':
    gunicorn_logger = logging.getLogger('gunicorn.error')
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)
