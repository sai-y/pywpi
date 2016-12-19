#!/usr/bin/python3
"""
	Flask framework
"""
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    author = "Me"
    name = "You"
    return render_template('index.html', author=author, name=name)

if __name__ == "__main__":
    app.run('0.0.0.0')