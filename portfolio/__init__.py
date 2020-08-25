#!/usr/bin/env python3

from flask import Flask

from portfolio import api, gui


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.logger.info('Flask app instantiated')
    app.register_blueprint(api.siteapi)
    app.logger.info('registered blueprint: siteapi')
    app.register_blueprint(api.swaggerblueprint, url_prefix=api.swaggerurl)
    app.logger.info('registered blueprint: swagger ui')
    app.register_blueprint(gui.sitegui)
    app.logger.info('registered blueprint: guiblueprint')
    return app


app = create_app()
app.logger.info('Application started successfully')
