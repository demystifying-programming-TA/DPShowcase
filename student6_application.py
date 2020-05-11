from flask import Flask
application = Flask(__name__)

@application.route("/home")
def home_view():
    return "*** Coming Soon ***"