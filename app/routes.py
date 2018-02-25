from app import app
from flask import request
import postgresql
from flask import jsonify
import json

@app.route('/')

@app.route('/index', methods = ['GET', 'POST'])
def index():
    if(request.method == 'GET'):
        return 'GET ACCEPTED'
    elif(request.method == 'POST'):
        return 'POST ACCEPTED'

@app.route('/login', methods = ['GET', 'POST'])
def login():
    if(request.method != 'POST'):
        return 'Request is not allowed, use POST'
    else:
        # postgres_obj = postgresql.PostgreSQL()
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

        return jsonify(
            msg=json.dumps(login_dictionary)
        )
        # return postgres_obj.authenticate(login_dictionary)

@app.route('/signup', methods = ['POST'])
def signup():
    postgres_obj = postgresql.PostgreSQL()
    signup_dictionary = {}

    if('username' in request.form):
        signup_dictionary['username'] = request.form['username']
    else:
        return 'Missing parameter - username'

    if('email' in request.form):
        signup_dictionary['email'] = request.form['email']
    else:
        return 'Missing parameter - email'

    if('password' in request.form):
        signup_dictionary['password'] = request.form['password']
    else:
        return 'Missing parameter - password'

    return postgres_obj.insert_user(signup_dictionary)
