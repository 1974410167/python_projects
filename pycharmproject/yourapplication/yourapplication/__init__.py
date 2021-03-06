from flask import Flask

app = Flask(__name__)

from views import bp

app.register_blueprint(bp)

if __name__ == '__main__':
    app.run(debug=True)