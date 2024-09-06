from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "testgh554eurdfg56374764fdggdfhf"


@app.route("/hello")
def index():
    flash("Whats your name?")
    return render_template("index.html")


@app.route("/greet", methods=["POST", "GET"])
def greet():
    flash("Hi " + str(request.form["name_input"]) + ", great to see you!")
    return render_template("index.html")
