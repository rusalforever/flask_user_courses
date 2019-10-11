from flask import Blueprint

user_course = Blueprint('user_course', __name__, template_folder='templates/')
from . import views
