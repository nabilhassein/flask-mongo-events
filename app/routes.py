import os
from app import app
from flask import render_template, request, redirect
from flask_pymongo import PyMongo

app.config['MONGO_DBNAME'] = 'database'
app.config['MONGO_URI'] = 'mongodb+srv://admin:upperline2019@cluster0-n3alx.mongodb.net/database?retryWrites=true&w=majority'
app.secret = b'insecure session verification'

mongo = PyMongo(app)


@app.route('/')
@app.route('/index')
def index():
    collection = mongo.db.events
    events = collection.find({})
    return render_template('index.html', events = events)


@app.route('/add')
def add():
    events = mongo.db.events

    events.insert({'event': 'homecoming', 'date': '2019-05-21'})
    
    return "added"


@app.route('/events/new', methods=['GET', 'POST'])
def new_event():
    if request.method == "GET":
        return render_template('new_event.html')

    event_name = request.form['event_name']
    event_date = request.form['event_date']
    user_name = request.form['user_name']

    events = mongo.db.events
    events.insert({
        'event': event_name,
        'date': event_date,
        'user': user_name
    })
    return redirect('/')


# @app.route('/signup', methods=['POST', 'GET'])
# def signup():
#     if request.method == 'POST':
#         users = mongo.db.users
#         existing_user = users.find_one({'name' : request.form['username']})

#         if existing_user is None:
#             users.insert({
#                 'name' : request.form['username'],
#                 'password' : request.form['password']
#             })
#             session['username'] = request.form['username']
#             return redirect(url_for('index'))

#         return 'That username already exists! Try logging in.'

#     return render_template('signup.html')
