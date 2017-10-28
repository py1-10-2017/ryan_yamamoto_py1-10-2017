from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
app.secret_key = "my key"
mysql = MySQLConnector(app,'full_friends')
import re
import datetime
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

@app.route('/')
def index():
    all_friends = mysql.query_db("SELECT * FROM friends;")
    return render_template('index.html', friends=all_friends)

@app.route('/friends', methods=['POST'])
def create():
    query_string = "INSERT INTO friends (first_name, last_name, email, created_at, updated_at)\
                    VALUES (:new_first_name, :new_last_name, :new_email, NOW(), NOW())"

    data_dict = {
        "new_first_name": request.form['first_name'],
        "new_last_name": request.form['last_name'],
        "new_email": request.form['email'],
        }
    mysql.query_db(query_string, data_dict)
    return redirect('/')

@app.route('/friends/<friend_id>/edit')
def edit(friend_id):
    query_string = "SELECT * FROM friends WHERE id = :the_id"
    data_dict = {"the_id": friend_id}
    try:
        one_friend = mysql.query_db(query_string, data_dict)[0]
    except IndexError:
        return redirect('/')
    return render_template('edit.html', friend=one_friend)

@app.route('/friends/<friend_id>', methods=['POST'])
def update(friend_id):
    query_string = "UPDATE friends SET first_name = :updated_first_name, last_name = :updated_last_name, email = :updated_email WHERE id = :the_id"
    data_dict = {
            "the_id": friend_id,
            "updated_first_name": request.form['first_name'],
            "updated_last_name": request.form['last_name'],
            "updated_email": request.form['email'],
            }
    mysql.query_db(query_string, data_dict)
    return redirect('/')

@app.route('/friends/<friend_id>/delete')
def delete(friend_id):
    query_string = "DELETE FROM friends WHERE id = :the_id"
    data_dict = {
        "the_id": friend_id
        }
    mysql.query_db(query_string, data_dict)
    return redirect('/')
app.run(debug=True)
