#!/usr/bin/env python
#coding:utf8

import os

from config import config
from modles import db
from flask import Flask
from flask.ext.login import LoginManager


login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

@login_manager.user_loader
def load_user(user_id):
    return UserModel.query.get(int(user_id))

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    db.init_app(app)
    login_manager.init_app(app)

    if not app.debug and not app.testing and not app.config['SSL_DISABLE']:
        from flask.ext.sslify import SSLify
        sslify = SSLify(app)

    from controller.router import router
    app.register_blueprint(router, url_prefix='')

    return app

if __name__ == '__main__':
    app = create_app(os.getenv('FLASK_CONFIG') or 'default')
    app.run(host='127.0.0.1')