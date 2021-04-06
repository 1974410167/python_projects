import os
from flask_script import Manager
from App import create_app

env = os.environ.get('FLASK_ENV')

manage = create_app(env)


if __name__ == '__main__':
    manage.run(debug=True)


