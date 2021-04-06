
from flask import Blueprint,render_template


bp = Blueprint('blue',__name__)

@bp.route('/')
def hello_world():
    return 'hello world'

@bp.route('/index')
def index():
    data = {
        'name':'hong',
        'age':134
    }
    return render_template('index.html',data=data)

@bp.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404