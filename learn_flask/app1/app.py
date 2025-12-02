from flask import Flask

app = Flask(__name__)
@app.route("/")
def index():
    return '<!DOCTYPE html><html lang= "en"><head></head><body><h1>Today will be a good day</h1></body></html>'

def index_0():
    return "hello, world"
