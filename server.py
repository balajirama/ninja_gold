from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'darksecret'

import random
import datetime

DATA = {
    'farm':[10,20],
    'cave':[5,10],
    'house':[2,5],
    'casino':[-50,50],
}

@app.route("/")
def root():
    if 'total_gold' not in session:
        session['total_gold'] = 0
        session['log'] = list()
    activity_log = session['log']
    activity_log.reverse()
    return render_template("game.html", DATA=DATA, activity_log=activity_log)

@app.route("/process_money", methods=['POST'])
def process_money():
    now = datetime.datetime.now()
    act = request.form['activity']
    gain = random.randint(DATA[act][0], DATA[act][1])
    session['total_gold'] += gain
    session['log'].append({'activity': act, 'time': now.strftime("%B %d, %Y at %I:%M:%S%p"), 'gain': gain})
    return redirect("/")

@app.route("/reset")
def reset():
    session.clear()
    return redirect("/")

if __name__ == '__main__':
    app.run(debug=True)
