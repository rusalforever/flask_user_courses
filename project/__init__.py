from flask import Flask
from flask_mysqldb import MySQL
from .config import run_config
from project.user_course import user_course

db = MySQL()


def run_app():
    app = Flask(__name__)
    app.config.from_object(run_config())

    db.init_app(app)
    app.register_blueprint(user_course)
    return app

# @app.errorhandler(Exception)
# def error(e):
#     return 'Something went wrong'
