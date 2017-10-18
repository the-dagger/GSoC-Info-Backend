from flask import Flask
from flask_sqlalchemy import SQLAlchemy

flask = Flask(__name__)
flask.config.from_object('config')
db = SQLAlchemy(flask)

from app import views, models