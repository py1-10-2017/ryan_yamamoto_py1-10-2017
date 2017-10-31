from flask import Flask, render_template, redirect, request, session, flash
from mysqlconnection import MySQLConnector
from flask_bcrypt import Bcrypt
import re
import datetime
app = Flask(__name__)
bcrypt = Bcrypt(app)
app.secret_key = 'secret_key'
mysql = MySQLConnector(app, 'database_diagram')
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')


@app.route('/')
def index():
    if 'logged' in session.keys():
        messages = mysql.query_db("SELECT * FROM messages ORDER BY created_at DESC")
        for message in messages:
            query = "SELECT * FROM users WHERE id=:the_user_id"
            data = {
                'the_user_id': message['user_id']
                }
            user = mysql.query_db(query, data)
            user = user[0]
            message['first_name'] = user['first_name']
            message['last_name'] = user['last_name']
            query = "SELECT * FROM comments WHERE message_id=:the_message_id ORDER BY created_at"
            data = {
                'the_message_id': message['id']
                }
            comments = mysql.query_db(query, data)
            for comment in comments:
                query = "SELECT * FROM users WHERE id=:the_user_id"
                data = {
                    'the_user_id': comment['user_id']
                    }
                user = mysql.query_db(query, data)
                user = user[0]
                comment['first_name'] = user['first_name']
                comment['last_name'] = user['last_name']
                message['comments'] = comments

        return render_template("wall.html", messages=messages)
    return render_template("index.html")

@app.route('/message', methods=['POST'])
def post_message():
    query = "INSERT INTO messages (message, user_id, created_at, updated_at) VALUES (:message, :user_id, NOW(), NOW());"
    data = {'message': request.form['message'], 'user_id': session['user_id']}
    mysql.query_db(query, data)
    return redirect('/')

@app.route('/comment', methods=['POST'])
def post_comment():
    query = "INSERT INTO comments (comment, user_id, message_id, created_at, updated_at) VALUES (:comment, :user_id, :message_id, now(), now());"
    data = {'comment': request.form['comment'], 'user_id': session['user_id'], 'message_id': request.form['message_id']}
    mysql.query_db(query, data)
    return redirect('/')

@app.route('/register', methods=['POST'])
def register():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']
    password = request.form['password']
    confirm_password = request.form['confirm_password']
    hashed_pw = bcrypt.generate_password_hash(password)
    errors = []
    valid = True
    if first_name == "":
        flash("First Name can't be empty and must have at least 2 letters")
        valid = False
    if last_name == "":
        flash("Last Name can't be empty and must have at least 2 letters")
        valid = False
    if email == "":
        flash("Must have a valid email")
        valid = False
    elif not EMAIL_REGEX.match(email):
        flash("Email must be valid format")
        valid = False
    if password == "":
        flash("Password can't be empty")
        valid = False
    elif confirm_password != password:
        flash("Password must match")
        valid = False
    if valid == True:
        query = "INSERT INTO users (first_name, last_name, email, password, created_at, updated_at)\
                VALUES (:one, :two, :three, :four, NOW(), NOW());"
        data = {
            "one": first_name,
            "two": last_name,
            "three": email,
            "four": hashed_pw
            }
        mysql.query_db(query, data)
        return redirect('/')
    if valid == False:
        return redirect('/')

@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']
    query = "SELECT * FROM users WHERE email=:the_email"
    data = {
        'the_email': email
        }
    user = mysql.query_db(query, data)
    user = user[0]
    if len(user) != 0 and bcrypt.check_password_hash(user['password'], password):
        session['logged'] = True
        session['user_id'] = user['id']
        session['first_name'] = user['first_name']
        session['last_name'] = user['last_name']
        return redirect('/')
    else:
        flash("Login Failed")
        return render_template("index.html")

@app.route('/logout')
def clear_session():
  session.clear()
  return redirect("/")

app.run(debug=True)
