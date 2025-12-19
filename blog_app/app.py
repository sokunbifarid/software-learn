from flask import Flask, render_template, request

app = Flask(__name__)

if __name__ == "__main__":
    app.run(debug=True)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/reader/<publisher>/<id>", methods=["GET"])
def reader(publisher, id):
    pass

@app.route("/publisher/login", methods=["GET"])
def publisher_login():
    pass

@app.route("/publisher/register", methods=["GET", "POST"])
def publisher_register():
    pass

@app.route("/publisher/forgot_password", methods=["GET", "POST"])
def publisher_forgot_password():
    pass

@app.route("/publisher/recovered_password", methods=["GET"])
def recovered_password():
    pass

@app.route("/publisher/edit_post/<id>", methods=["GET","POST", "PUT"])
def publisher_edit_post():
    #this section is for showing the post and edit, if the id is null, then
    #it will load writing a new post and if it is not then it is an edit.
    pass

@app.route("/publisher/publish_list", methods=["GET"])
def publisher_post_list():
    pass


