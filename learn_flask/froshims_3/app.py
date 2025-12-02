from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

#db = SQL("sqlite:///froshims.db")

SPORTS = ["BASKETBALL", "SOCCER", "ULTIMATE FRISBEE"]

def get_db_connection():
    conn = sqlite3.connect("froshims.db")
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/")
def index():
    return render_template("index.html", sports=SPORTS)

@app.route("/deregister", methods=["POST"])
def deregister():
    id = request.form.get("id")
    if id:
        conn = get_db_connection()
        db = conn.execute("DELETE FROM registratnts WHERE id=?", id)
        conn.close()
    return redirect("/registrants")

@app.route("/register", methods=["POST"])
def register():
    name = request.form.get("name")
    if not name:
        return render_template("error.html", message="Missing name")

    sports = request.form.getlist("sport")
    if not sports:
        return render_template("error.html", message= "Missing Sport")
    for sport in sports:
        if sport not in SPORTS:
            return render_template("error.html", message="Invalid sport")
    for sport in sports:
        conn = get_db_connection()
        conn.execute("INSERT INTO registrants (name, sport) VALUES(?, ?)", (name, sport))
        print(conn.execute("SELECT * FROM registrants").fetchall())
        conn.close()
    return redirect("/registrants")

@app.route("/registrants")
def registrants():
    conn = get_db_connection()
    registrants = conn.execute("SELECT * FROM registrants").fetchall()
    conn.close()
    return render_template("registrants.html", registrants=registrants)
