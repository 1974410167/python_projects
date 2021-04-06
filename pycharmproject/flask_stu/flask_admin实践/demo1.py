import os
basedir = os.path.abspath(os.path.dirname(__file__))

from flask import Flask
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'hard to guess string'

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(16))


admin = Admin(app,name='后台管理系统')


admin.add_view(ModelView(User,db.session))

@app.route('/create_db')
def create_db():
    db.create_all()
    return None

app.run(debug=True)

