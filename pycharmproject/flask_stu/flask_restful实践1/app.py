from flask import Flask
app = Flask(__name__)

import datetime as dt
from pprint import pprint
from marshmallow import Schema,fields,post_load,ValidationError,validates

class User:
    def __init__(self,name,email):
        self.name = name
        self.email = email
        self.created_at = dt.datetime.now()

    def __repr__(self):
        return f"<User>(name={self.name})"

class UserSchema(Schema):
    name = fields.Str()
    email = fields.Email()
    created_at = fields.DateTime()
    @post_load
    def make_user(self,data,**kwargs):
        return User(**data)
    @validates("name")
    def validate_name(self,t):
        if len(t)<3:
            raise ValidationError('the name must be greater than 3')


user = User(name='Monty',email='Monty@python.prg')
schame = UserSchema(only=('name','email'))
result = schame.dump(user)
pprint(result)

# user_data = [
#     {"email": "mick@stones.com", "name": "Mi2"},
#     {"email": "keith@stones.com", "name": "Keith"},
# ]
#
# schame = UserSchema(many=True)
#
# try:
#     result = schame.load(user_data)
#     print(result)
#     print(type(result))
#
# except ValidationError as err:
#     print(err.messages)
#     print(err.valid_data)


# ss = UserSchema()
# result = ss.load(user_data)
# pprint(result)

# @app.route('/')
# def hello_world():
#     return 'Hello, World!'
