import os

from flask import Blueprint, Flask
from flask_sqlalchemy import SQLAlchemy

from .views import init_views
from .model import init_models

basedir = os.path.abspath(os.path.dirname(__file__))

def create_app():
    
    myapp = Flask(__name__)

    init_views(myapp)

    myapp.config['SQLALCHEMY_DATABASE_URL'] = 'sqlite:///'+os.path.join(basedir,'app1.db')
    myapp.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    myapp.config['SQLALCHEMY_COMMIT_TEARDOWN'] = True

    init_models(myapp)
    
    

    return myapp

