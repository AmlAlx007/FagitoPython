from flask import Flask

app = Flask(__name__)


@app.route("/amalu")
def hello():
    return '<h1>Hello!</h1>'

