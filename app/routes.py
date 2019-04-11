from app import app
from app.forms import LoginForm
from flask import render_template, flash, redirect
@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'nikhil'}
    posts = [{'author': {'username': 'John'}, 'body': 'Photography is awesome'},
             {'author': {'username': 'Jane'}, 'body': 'Avengers was good'}]
    return render_template('index.html', user=user, posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, ')
    return render_template('login.html', title='Sign In', form=form)
