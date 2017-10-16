from flask import Flask, render_template, request, redirect, flash
app = Flask(__name__)
app.secret_key = "ryans key"

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/users', methods=['POST'])
def create_user():
    print "Got Post Info"
    name = request.form['name']
    location = request.form['location']
    language = request.form['language']
    comment = request.form['comment']
    valid = True
    if name == "":
        valid = False
        flash("name is empty")
    if comment == "":
        valid = False
        flash("comment is empty")
    elif len(comment) > 120:
        valid = False
        flash("comment is longer than 120")

    if valid:
        return redirect('/display')
    if not valid:
        return redirect('/')

@app.route('/display', methods=['POST'])
def display():
    return render_template("submit.html", name=name, location=location, language=language, comment=comment)
app.run(debug=True)
