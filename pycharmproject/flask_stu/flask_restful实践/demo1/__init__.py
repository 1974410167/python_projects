import os
from flask import Flask
from flask_restful import Resource,Api
from .models import init_models
from .rest_view import init_restful

basedir = os.path.abspath(os.path.dirname(__file__))

def create_app():

    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir,'app.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'hard to guess string'
    app.config['JSON_AS_ASCII'] = False

    init_models(app)

    init_restful(app)

    return app


