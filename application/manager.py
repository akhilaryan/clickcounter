from application import app
from flask import render_template
from application.models import *


@app.route('/')
@app.route('/index/')
def index():
    return render_template('info/index.html', title='Click Counter')

@app.route('/count')
def count():
	return render_template('info/count.html', title = 'Click count')

# @app.route('/hello/<username>/')
# def hello_username(username):
#     return render_template('info/hello.html', title="Flask-Bootstrap, Hi %s"
#                             % (username), username=username)
