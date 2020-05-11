# ----------------------------------------------------------------------- #

# DPShowcase

# File:         application.py
# Maintainer:   DP Team
# Last Updated: 2020-04-13
# Language:     Python 3.7

# ------------------------------------------------------------------------ #

# ------------------------------------------------------------------------ #
# Initialization
# ------------------------------------------------------------------------ #

# Load external dependencies
# ---------------------------------------------#
from flask import Flask
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from werkzeug.serving import run_simple

# Load internal dependencies
# ---------------------------------------------#
from main_application import application as main_app
from demo_application import application as demo_app
from student1_application import application as student1_app
from student2_application import application as student2_app
from student3_application import application as student3_app
from student4_application import application as student4_app
from student5_application import application as student5_app
from student6_application import application as student6_app
from student7_application import application as student7_app

# Initialize flask app
# ---------------------------------------------#
application = Flask(__name__)
application.wsgi_app = DispatcherMiddleware(main_app, {
    '/demo':demo_app,
    '/student1': student1_app,
    '/student2': student2_app,
    '/student3': student3_app,
    '/student4': student4_app,
    '/student5': student5_app,
    '/student6': student6_app,
    '/student7': student7_app,
})


# ------------------------------------------------------------------------ #
# Run
# ------------------------------------------------------------------------ #
if __name__ == "__main__":
	application.run()

# ------------------------------------------------------------------------ #
# ------------------------------------------------------------------------ #
