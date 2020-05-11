from flask import Flask
application = Flask(__name__)


# bye_world_app.py
@application.route("/")
def hello():
    return "Hello World!"