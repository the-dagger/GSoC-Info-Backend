from app import flask, db
from flask import render_template, flash, redirect, abort, jsonify, request, make_response
from .forms import LoginForm
import json
import models

@flask.route('/')
@flask.route('/index')
def index():
    return render_template('index.html')

@flask.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID="%s", remember_me=%s' %
              (form.openid.data, str(form.remember_me.data)))
        return redirect('/index')
    return render_template('login.html', 
                           title='Sign In',
                           form=form,
                           providers=flask.config['OPENID_PROVIDERS'])

@flask.route('/user/<string:uid>/')
def get_dev(uid):
    u = models.User.query.get(uid)
    return to_json(u)

@flask.route('/post/register/', methods = ['POST'])
def create_dev():
    if not request.json or not 'uid' in request.json:
        abort(400)
    u = models.User(request.json.get('uid'), request.json.get('name'), request.json.get('email'), request.json.get('college'), request.json.get('branch'),
    request.json.get('specialization'), request.json.get('is_mentor',''), request.json.get('cert_link', ''),
    request.json.get('profile_image'), request.json.get('organization',''), request.json.get('year', ''))
    db.session.add(u)
    db.session.commit()
    return make_response(to_json(u), 201)

@flask.route('/users/', methods = ['GET'])
def get_all():
    users = models.User.query.all()
    user_list = []
    for u in users:
        user_list.append(to_json(u))
    temp = ", ".join(user_list)
    # TODO : Use better logic here
    return "{ \"users\" : [" + temp + "] }"

def to_json(u):
    data = {"uid":u.uid, "name":u.name, "email":u.email, "college":u.college, "branch":u.branch, "specialization":u.specialization, "is_mentor":u.is_mentor, 
"cert_link":u.cert_link, "profile_image":u.profile_image, "organization":u.organization, "year":u.year}
    return json.dumps(data)