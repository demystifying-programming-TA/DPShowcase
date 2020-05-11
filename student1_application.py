from flask import Flask
application = Flask(__name__)


# hello_world_app.py
@application.route("/")
def hello():
    return "Student1!"