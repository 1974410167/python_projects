from flask import Blueprint
from .model import models

bp1 = Blueprint('blue',__name__)

bp2 = Blueprint('bule2',__name__)

def init_views(app):

    app.register_blueprint(bp1)
    app.register_blueprint(bp2)

@bp1.route('/name')
def name():
    return f"name+{__name__}"

@bp2.route('/create_db')
def create_db():

    models.create_all()

    return "数据库创建成功"
@bp2.route('/dropall_db')
def dropall_db():

    models.drop_all()

    return "数据库删除成功"



@bp2.route('/age')
def age():
    return "age is 19"