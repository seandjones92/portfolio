#!/usr/bin/env python3

from flask import Flask
from portfolio import api, gui
import logging


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.register_blueprint(api.siteapi)
    app.register_blueprint(api.swaggerblueprint, url_prefix=api.swaggerurl)
    app.register_blueprint(gui.sitegui)

    return app


app = create_app()

if __name__ != '__main__':
    gunicorn_logger = logging.getLogger('gunicorn.error')
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)
