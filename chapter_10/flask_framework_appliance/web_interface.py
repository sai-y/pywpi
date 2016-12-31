#!/usr/bin/python3
"""
    Flask framework
"""
from flask import Flask, render_template, request, redirect
from gpiozero import OutputDevice

relay_index = [2,3,4,5]
relay = []
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('index.html')

@app.route('/energize', methods = ['POST'])
def energize():
    value = request.form["relay"]
    print(value)
    return redirect('/')

if __name__ == "__main__":
    app.run('0.0.0.0')