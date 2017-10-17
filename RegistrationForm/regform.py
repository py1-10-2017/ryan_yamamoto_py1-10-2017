
from flask import Flask, render_template, session, request, redirect, flash
import re
app = Flask(__name__)
app.secret_key = 'secretkey'

@app.route('/')
def index():
    return render_template('/index.html')

@app.route('/register', methods=['POST'])
def register():
    email = request.form['email']
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    password = request.form['password']
    confirm_password = request.form['confirm_password']
    valid = True

    if len(email) < 1:
        flash('Email cannot be empty')
        valid = False
    if len(first_name) < 1:
        flash('First name cannot be empty')
        valid = False
    if len(last_name) < 1:
        flash('Last name cannot be empty')
        valid = False
    if len(password) < 8:
        flash('Password must be at least 8 characters')
        valid = False
    if password != confirm_password:
        flash('Password does not match')
        valid = False

    if valid == True:
        return redirect('/success')
    if valid == False:
        return redirect('/')

@app.route('/success')
def success():
    return render_template('/success.html')






app.run(debug=True)
