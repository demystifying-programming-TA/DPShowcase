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

# Initialize flask app
# ---------------------------------------------#
application = Flask(__name__)
application.wsgi_app = DispatcherMiddleware(main_app, {
    '/demo':demo_app,
    '/student1': student1_app,
})


# ------------------------------------------------------------------------ #
# Run
# ------------------------------------------------------------------------ #
application.run()

# ------------------------------------------------------------------------ #
# ------------------------------------------------------------------------ #
