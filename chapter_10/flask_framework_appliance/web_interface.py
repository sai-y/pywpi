#!/usr/bin/python3
"""
    Flask framework
"""
from flask import Flask, render_template, request, redirect
from gpiozero import OutputDevice

relay_index = [2,3,4,5]
devices = []
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('index.html')

@app.route('/energize', methods = ['POST'])
def energize():
    if request.form is not None: 
        relays = request.form
        print(relays)
        return redirect('/')

if __name__ == "__main__":
    app.run('0.0.0.0')