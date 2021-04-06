

from app1 import create_app
from flask_script import Manager

app = create_app()

manager = Manager(app)
manager.add_command('db','MigrateCommand')

if __name__ == '__main__':
    app.run(debug=True)
