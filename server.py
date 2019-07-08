from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'darksecret'

import random

DATA = {
    'farm':[10,20],
    'cave':[5,10],
    'house':[2,5],
    'casino':[-50,50],
}

@app.route("/")
def root():
    return render_template("game.html", DATA=DATA)

@app.route("/process_money", methods=['POST'])
def process_money():
    return redirect("/")

if __name__ == '__main__':
    app.run(debug=True)
