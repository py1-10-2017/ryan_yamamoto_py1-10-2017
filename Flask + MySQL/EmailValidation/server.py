from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
app.secret_key = "my key"
mysql = MySQLConnector(app,'email_valid')
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')


@app.route('/success')
def success():
    all_email = mysql.query_db("SELECT * FROM users;")
    return render_template('success.html', email_address=all_email)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create', methods=['POST'])
def create():
    if not EMAIL_REGEX.match(request.form['email']):
        flash('Invalid Email.')
        return redirect('/')
    else:
        query_string = "INSERT INTO users (email, created_at, updated_at)\
                        VALUES (:new_email, NOW(), NOW())"
        data_dict = {
                'new_email':request.form['email']
                }
        mysql.query_db(query_string, data_dict)
    return redirect('/success')

app.run(debug=True)
