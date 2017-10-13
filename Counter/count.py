from flask import Flask, render_template, session, redirect, request
app = Flask(__name__)
app.secret_key = "secret key"


@app.route('/')
def index():
    session['count'] += 1
    return render_template('index.html')


@app.route('/double')
def double():
    session['count'] += 1
    return redirect('/')

@app.route('/reset')
def reset():
    session['count'] = -1
    return redirect('/')


app.run(debug=True)
