from flask import Flask
from os import getenv


def init_app(app: Flask):
    app.config["SQLALCHEMY_DATABASE_URI"] = getenv("SQLALCHEMY_DATABASE_URI")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["JSON_SORT_KEYS"] = False
    app.config["SECRET_KEY"] = getenv("SECRET_KEY")
    app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024