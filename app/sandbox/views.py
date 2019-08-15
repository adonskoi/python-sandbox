from pathlib import Path
from flask import Blueprint, send_file
from docx import Document

from app import db

# Define the blueprints
sandbox = Blueprint('sandbox', __name__, url_prefix='/sandbox')


@sandbox.route('/')
def hello():
    return "hello from sandbox"


@sandbox.route('/doc')
def _():
    name = create_doc()
    return send_file(name)


def create_doc():
    document = Document()
    document.add_paragraph('Lorem ipsum dolor sit amet.')
    path = Path().absolute()
    name = f"{path}/document.docx"
    document.save(name)
    return name