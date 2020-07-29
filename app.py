from flask import Flask, request, redirect, url_for, render_template

app = Flask(__name__)


@app.route('/login', methods=['POST', 'GET'])
def Login():
    if request.method == "POST":
	user = request.form["nm"]
	return redirect(url_for("user", usr=user))
    else:
	return render_template("login.html")

@app.route("/<usr>")
def user(usr):
    return f"<h1>{usr}</h1>"

if __name__ == '__main__':
    # Used when running locally only. When deploying to Cloud Run,
    # a webserver process such as Gunicorn will serve the app.
    app.run(host='localhost', port=8080, debug=True)
