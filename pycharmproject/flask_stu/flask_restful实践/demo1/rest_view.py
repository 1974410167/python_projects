
from flask_restful import Resource,Api,reqparse,abort
from .models import User,models
from flask import request
import json

api = Api()

def abort_if_todo_doesnt_exist(todo_id):

    User_list = User.query.all()
    if todo_id not in User_list:
        abort(404,message=f"user{todo_id} does't exist.")


parse = reqparse.RequestParser()
parse.add_argument('name')


def init_restful(app):
    api.init_app(app)


class Helloworld(Resource):
    def get(self):
        return {'hello':'world'}



class TodoSimple(Resource):
    def get(self,todo_id):
        user = User.query.get(todo_id)
        return {todo_id:user.name}

    def put(self,todo_id):
        args = parse.parse_args()
        name = args['name']

        user = User.query.get(todo_id)
        user.name = name
        models.session.add(user)
        models.session.commit()
        return 'upgrade successful'

    def delete(self,todo_id):

        user = User.query.filter_by(id=todo_id).first()
        models.session.delete(user)
        models.session.commit()

        return 'delete successful'

parse = reqparse.RequestParser()
parse.add_argument('name')

class TodoList(Resource):
    def get(self):
        return {"sss":"sssssss"}

    def post(self):
        args = parse.parse_args()
        name = args['name']

        t = User(name=name)
        models.session.add(t)
        models.session.commit()

api.add_resource(TodoList,'/todos')
api.add_resource(TodoSimple,'/<int:todo_id>')
api.add_resource(Helloworld,'/')


