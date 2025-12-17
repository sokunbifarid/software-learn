from flask import Flask, render_template, request

app = Flask(__name__)

if __name__ == "__main__":
    app.run(debug=True)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")
