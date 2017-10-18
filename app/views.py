from app import flask
from flask import render_template

@flask.route('/')
@flask.route('/index')
def index():
    return render_template('index.html')