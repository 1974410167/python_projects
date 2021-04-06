# from flask import
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import MigrateCommand,Migrate

models = SQLAlchemy()

migrate = Migrate()


def init_models(app):
    
    models.init_app(app)
    migrate.init_app(app,models)


class User(models.Model):
    id = models.Column(models.Integer,primary_key=True)
    name = models.Column(models.String(16))
