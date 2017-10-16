from flask import Flask, render_template, session, redirect, request
app = Flask(__name__)
app.secret_key = "secret key"
from datetime import datetime
import random


@app.route('/')
def index():
    try:
        session['mygold']
    except KeyError:
        session['mygold'] = 0
    return render_template('index.html')

@app.route('/process', methods=["POST"])
def process():
    try:
        temp = session['activity']
    except KeyError:
        temp = []

    if request.form['building'] == 'farm':
        result = random.randint(10,21)

    elif request.form['building'] == 'cave':
        result = random.randint(5,11)

    elif request.form['building'] == 'house':
        result = random.randint(2,6)

    elif request.form['building'] == 'casino':
        result = random.randint(-50,51)

    message = "You earned/lost {} at {}".format(result, datetime.now().strftime("%B, %d at %H:%m:%p"))
    session['mygold'] = int(session['mygold']) + result
    temp.append(message)
    session['activity'] = temp
    return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
    session.clear()
    return redirect('/')


app.run(debug=True)
