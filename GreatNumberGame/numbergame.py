from flask import Flask, render_template, session, redirect, request
app = Flask(__name__)
app.secret_key = "secret key"
import random


@app.route('/')
def index():
    if not "correct_number" in session.keys():
        session["correct_number"] = random.randrange(0, 101)
    if "current_state" in session.keys():
        return render_template("display.html")
    else:
        return render_template('index.html')

@app.route('/process', methods=["POST"])
def process():
    print request.form["guess"]
    print session["correct_number"]
    if int(request.form["guess"]) == session["correct_number"]:
        session["current_state"] = "correct!"
    elif int(request.form["guess"]) > session["correct_number"]:
        session["current_state"] = "too high"
    else:
        session["current_state"] = "too low"
    return redirect("/")

app.run(debug=True)
