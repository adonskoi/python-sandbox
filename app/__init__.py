import os

from flask import Flask

# Define the WSGI application object
app = Flask(__name__)

# Configurations
app.config.from_object('config')

# Define the database

from pymongo import MongoClient

mongo_connection_string = os.environ.get(
    'MONGO_SRV_STRING') or "localhost:27017"
client = MongoClient(mongo_connection_string)
db = client.sandbox


# Sample HTTP error handling
@app.errorhandler(404)
def not_found(error):
    return 'not found'


@app.route('/')
def home() -> str:
    return "Hello world"


# Import a module / component using its blueprint
from app.mod_auth.views import mod_auth as auth_module
from app.sandbox.views import sandbox as sandbox_module

# Register blueprints
app.register_blueprint(auth_module)
app.register_blueprint(sandbox_module)
