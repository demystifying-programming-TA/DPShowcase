# ------------------------------------------------------------------------ #
# Initialization
# ------------------------------------------------------------------------ #

# Load dependencies
# ---------------------------------------------#
import flask

import sys
sys.path.append('backend/student4')
import dataprocessing as dp

application = flask.Flask(__name__, template_folder = 'frontend/student4', static_folder = 'frontend/student4')

# ------------------------------------------------------------------------ #
# Test Functions
# ------------------------------------------------------------------------ #

## Try the location_mobility_data() function
## Note: Longitude,latitude refer to the United States
#data = dp.location_mobility_data(longitude = -71.08328259999999, latitude = 42.3662154)
#print("Country name: ", data[0])
#print("Decrease in # of walking calls (%): " + str(data[1]))
#print("Decrease in # of driving calls (%): " + str(data[2]))

#for i in [[-71.08328259999999, 42.3662154],[10.48328259999999, 51.3662154],[-1.78328259999999, 52.4662154]]:

#	try:
#		long = i[0]
#		lat = i[1]
#		data = dp.location_mobility_data(longitude = long, latitude = lat)
#		print("Country name: ", data[0])
#		print("Decrease in # of walking calls (%): " + str(data[1]))
#		print("Decrease in # of driving calls (%): " + str(data[2]))

#	except:
#		print("Country not found.")

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
# ---------------------------------------#

@application.route('/update_country')
def update_country_view():

	# Extract the data received from frontend
	long = flask.request.args.get('longitude')
	lat = flask.request.args.get('latitude')

	# Retrieve the location-specific data
	location_data = dp.location_mobility_data(longitude = long, latitude = lat)

	# Pass the data to the home page & updated page
	return flask.jsonify({"Country":location_data[0], "WalkingDecrease":location_data[1], "DrivingDecrease":location_data[2]})





