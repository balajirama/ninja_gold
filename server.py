from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'darksecret'

import random

@app.route("/")
def root():
    if 'number' not in session:
        session['number'] = random.randint(1,100)
        session['message'] = 'start'
        session['trials'] = 0
        session['placeholder'] = random.randint(1,100)
        session['oldguesses'] = list()
        session['wasted']=False
    print("inside root() before render_template()")
    return render_template("game.html")

@app.route("/guess", methods=['POST'])
def guess():
    print("inside guess() before everything")
    session['trials'] += 1
    try:
        session['guess']=int(request.form['guess'])
    except:
        session['guess']=session['placeholder']
    if session['guess'] in session['oldguesses']:
        session['wasted']=True
    else:
        session['wasted']=False
        session['oldguesses'].append(session['guess'])
    if session['guess']==session['number']:
        session['message'] = 'match'
    else:
        if session['guess'] > session['number']:
            session['message'] = 'high'
        else:
            session['message'] = 'low'
    session['placeholder'] = random.randint(1,100)
    print("inside guess() before redirect()")
    return redirect("/")

@app.route("/restart")
def restart():
    session.clear()
    return redirect("/")


if __name__ == '__main__':
    app.run(debug=True)
