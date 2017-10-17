from app import flask

@flask.route('/')
@flask.route('/index')
def index():
    return "Hello, World!"