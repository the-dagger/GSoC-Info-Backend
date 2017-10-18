from app import flask
from flask import render_template, flash, redirect
from .forms import LoginForm

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