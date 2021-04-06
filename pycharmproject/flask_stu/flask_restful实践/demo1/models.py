from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


models = SQLAlchemy()
migrate = Migrate()



def init_models(app):
    models.init_app(app)
    migrate.init_app(app,models)


class User(models.Model):
    id = models.Column(models.Integer, primary_key=True)
    name = models.Column(models.String(16))

    def __str__(self):
        return self.name