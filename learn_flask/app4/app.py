from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")
    else:
        name = request.form.get("name")
        return render_template("greet.html", name=name)

@app.route("/greet", methods=["GET"])
def greet():
    name = request.args.get("name", "world")
    return render_template("greet.html", name=name)

@app.route("/greet_encrypted", methods=["POST"])
def greet_encrypted():
    name = request.form.get("name")
    return render_template("greet.html", name=name)
