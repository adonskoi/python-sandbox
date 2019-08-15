from flask import Blueprint

from app import db

# Define the blueprints
mod_auth = Blueprint('auth', __name__, url_prefix='/auth')


@mod_auth.route('/')
def hello_from_auth():
    return "Hello from auth"


# @mod_auth.route('/test')
# def test_db():
#     all = db.weather.find_one({})
#     return f'temperature: {all["weather"]["t"]}'
