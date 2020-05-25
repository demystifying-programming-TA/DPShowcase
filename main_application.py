import flask
application = flask.Flask(__name__)


@application.route("/")
def index_view():
	return flask.redirect("https://demystifying-programming-ta.github.io/DP/#/dpproject/showcase")