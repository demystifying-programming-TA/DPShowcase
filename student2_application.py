# Load external dependencies
# ---------------------------------------------#
import flask

# Initialize the flask application
# ---------------------------------------------#
application = flask.Flask(__name__, 
	template_folder = 'frontend/student2', 
	static_folder = 'frontend/student2')

# ------------------------------------------------------------------------ #

# Load dependencies
# ---------------------------------------------#
import sys
sys.path.append('backend/student2')
import dataprocessing as dp

# ------------------------------------------------------------------------ #
# Test Functions
for i in [[0.1278,51.5074]]:
	long = i[0]
	lat = i[1]
	data = dp.location_mobility_data(longitude = long, latitude = lat)
	print("Country name: ", data[0])
	print("Decrease in # of walking calls (%): " + str(data[1]))
	print("Decrease in # of driving calls (%): " + str(data[2]))

# ------------------------------------------------------------------------ #
# Define views
# ------------------------------------------------------------------------ #

# home
# ---------------------------------------------#
@application.route('/home')
def home_view():

	# Render the home page
	return flask.render_template('index.html')

# ------------------------------------------------------------------------ #

## Try the location_mobility_data() function
## Note: Longitude,latitude refer to the United States


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
