from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    # For the sake of example, use static information to inflate the template.
    # This will be replaced with real information in later steps.
    print("Hello World!")
    return render_template("index.html")
