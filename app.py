from flask import Flask, redirect, url_for, render_template, request
import os
import json

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        fname = request.form["fname"]
        lname = request.form["lname"]
        user = fname + " " + lname
        dictuser = dict(fname=fname, lname=lname)
        return redirect(url_for("user", usr=str(json.dumps(dictuser))))
    else:
        return render_template("login.html")

@app.route("/<usr>")
def user(usr):
    return f"<h1>{usr}</h1>"

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
