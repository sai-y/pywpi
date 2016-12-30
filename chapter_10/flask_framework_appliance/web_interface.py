#!/usr/bin/python3
"""
    Flask framework
"""
from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route("/")
def hello():
    return render_template('index.html')

@app.route('/forward', methods = ['POST'])
def forward():
    return redirect('/')

@app.route('/reverse', methods = ['POST'])
def reverse():
    return redirect('/')

@app.route('/left', methods = ['POST'])
def left():
    return redirect('/')

@app.route('/right', methods = ['POST'])
def right():
    return redirect('/')

if __name__ == "__main__":
    app.run('0.0.0.0')