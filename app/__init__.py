from flask import Flask

flask = Flask(__name__)
flask.config.from_object('config')
from app import views