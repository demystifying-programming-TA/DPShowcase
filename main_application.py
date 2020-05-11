from flask import Flask
application = Flask(__name__)


@application.route("/")
def index_view():
	return redirect("https://demystifying-programming-ta.github.io/DP/#/dpproject/showcase")