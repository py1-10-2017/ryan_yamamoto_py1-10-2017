from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
from flask_bcrypt import Bcrypt
app = Flask(__name__)
bcrypt = Bcrypt(app)
app.secret_key = "my key"
mysql = MySQLConnector(app,'login_reg')
import re
import datetime
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9_.+_-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')

@app.route('/')
def index():
    if "id" in session.keys():
        return redirect('/success')
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']
    username = request.form['username']
    password = request.form['password']
    confirm_password = request.form['confirm_password']
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
    if username == "":
        flash("Username can't be empty and must have at least 2 letters")
        valid = False
    if password == "":
        flash("Password can't be empty and must have at least 8 characters")
        valid = False
    elif confirm_password != password:
        flash("Password must match")
        valid = False
    hashed_pw = bcrypt.generate_password_hash(password)
    if valid == True:
        query = "INSERT INTO users (first_name, last_name, email, username, password)\
                VALUES (:one, :two, :three, :four, :five);"
        data = {
            "one": first_name,
            "two": last_name,
            "three": email,
            "four": username,
            "five": hashed_pw
            }
        mysql.query_db(query, data)
        return redirect('/')
    if valid == False:
        return redirect('/')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    query = "SELECT * FROM users WHERE username=:one"
    data = {
        "one": username
        }
    user = mysql.query_db(query, data)
    if len(user) == 0:
        flash("This is not a real username")
        return redirect('/')
    else:
        user = user[0]
        if bcrypt.check_password_hash(user['password'], password):
            flash("Logged in!")
            session['id'] = user['id']
            return redirect('/success')
        else:
            flash("invalid")
            return redirect('/')
    return "hit login route"


@app.route('/success')
def success():
    query = "SELECT username FROM users WHERE id=:one"
    data = {
        "one": session['id']
        }
    logged_user = mysql.query_db(query, data)[0]
    return logged_user['username']

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')
app.run(debug=True)
