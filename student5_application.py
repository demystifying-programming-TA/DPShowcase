# Initialization
# ------------------------------------------------------------------------ #

# Load external dependencies
# ---------------------------------------------#
import flask

# Load internal dependencies
# ---------------------------------------------#
import sys
sys.path.append('backend/student5')
import dataprocessing as dp

# Initialize the flask application
# ---------------------------------------------#
application = flask.Flask(__name__, 
	template_folder = 'frontend/student5', 
	static_folder = 'frontend/student5')


# ------------------------------------------------------------------------ #
# Define views
# ------------------------------------------------------------------------ #

# home
# ---------------------------------------------#
@application.route('/home')
def home_view():

	# Render the home page
	return flask.render_template('index.html')
	
	
# update_country
# ---------------------------------------------#
@application.route('/update_country')
def update_country_view():

	# Extract the data received from frontend
	long = flask.request.args.get('longitude')
	lat  = flask.request.args.get('latitude')

	# Retrieve the location-specific data
	location_data = dp.location_mobility_data(longitude = long, latitude = lat)

	# Pass the data to the home page & updated page
	return flask.jsonify({"Country":location_data[0], "WalkingDecrease":location_data[1], 
		"DrivingDecrease":location_data[2]})


# ------------------------------------------------------------------------ #
# ------------------------------------------------------------------------ #