from app import app
from flask import request
import postgresql

@app.route('/')

@app.route('/index', methods = ['GET'])
def index():
    return 'Hello, World! - PaChill~~~'

@app.route('/login', methods = ['POST'])
def login():
    postgres_obj = postgresql.PostgreSQL()
    login_dictionary = {}

    if('password' in request.form):
        login_dictionary['password'] = request.form['password']
    else:
        return 'Missing parameter - password'

    if('username' in request.form):
        login_dictionary['username'] = request.form['username']
    elif('email' in request.form):
        login_dictionary['email'] = request.form['email']
    else:
        return 'Missing parameter - email/username'

    return postgres_obj.authenticate(login_dictionary)
