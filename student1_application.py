# ------------------------------------------------------------------------ #
# Initialization
# ------------------------------------------------------------------------ #

# Load dependencies
# ---------------------------------------------#
import sys
sys.path.append('backend/student1')
import airquality as aq
import requests
import numpy as np
import pandas as pd
import flask

application = flask.Flask(__name__,
    template_folder = 'frontend/student1',
    static_folder = 'frontend/student1')

# update_country
# ---------------------------------------------#
@application.route('/update_country')
def update_country_view():

    # Extract the data received from frontend
    long = []
    lat = []

    long = np.append(long, flask.request.args.get('longitude1'))
    lat  = np.append(lat,flask.request.args.get('latitude1'))
    long = np.append(long, flask.request.args.get('longitude2'))
    lat  = np.append(lat,flask.request.args.get('latitude2'))
    long = np.append(long, flask.request.args.get('longitude3'))
    lat  = np.append(lat,flask.request.args.get('latitude3'))

    data = []
    index = 0
    long=[-71.057083,-71.094,144.96]
    lat= [42.361145,42.36,-37.81]
    
    for i in range(0,3):
        # Retrieve the location-specific data
        print(long[i])
        try:
            #print(index)
            #long = i[0]
            #lat  = i[1]
            try:
                result = aq.location_mobility_data(longitude = long[i], latitude = lat[i], radius = 1000)
            except:
                try:
                    result = aq.location_mobility_data(longitude = long[i], latitude = lat[i], radius = 2500)
                except:
                    try:
                        result = aq.location_mobility_data(longitude = long[i], latitude = lat[i], radius = 10000)
                    except:
                        long=[-71.057083,-71.094,144.96]
                        lat= [42.361145,42.36,-37.81]
                        result = aq.location_mobility_data(longitude = long[i], latitude = lat[i], radius = 10000)


            print(result)
            #print("Location: ", result[0])
            #print("Dates: ", result[1])
            #print("Values: ", result[2])
            d = np.array(result[0],dtype = object)
            a = np.reshape(result[1],(-1,1))
            b = np.reshape(result[2],(-1,1))
            c = np.reshape(result[3],(-1,1))
            a = np.array(a,dtype=object)
            b = np.array(b,dtype=object)
            c = np.array(c,dtype=object)
            
            if index == 0:
                data = np.hstack((a,b,c))
                loc = d
            else:
                data = np.hstack((data,b,c))
                loc = np.append(loc,d)
        except:
            print("Error")
        index += 1
        #print(loc)
        #print(data)
    

    data = data.tolist()
    loc = loc.tolist()

    #data = np.array2string(data, separator= ', ')
    #print(data)
    # Pass the data to the home page & updated page
    return flask.jsonify({"Location":loc, "Data":data})


# ------------------------------------------------------------------------ #
# Test Functions
# ------------------------------------------------------------------------ #

## Try the location_mobility_data() function
## Note: Longitude,latitude refer to the United States


# data = []
# index = 0 
# ## Note: Try with US, Germany, UK
# for i in [[-122.42, 37.775],[153.03, -27.47],[-71.06, 42.36]]:
#     try:
#         long = i[0]
#         lat  = i[1]
        
#         result = aq.location_mobility_data(longitude = long, latitude = lat)
        
#         #print("Location: ", result[0])
#         #print("Dates: ", result[1])
#         #print("Values: ", result[2])

#         a = np.reshape(result[1],(-1,1))
#         b = np.reshape(result[2],(-1,1))
#         c = np.reshape(result[3],(-1,1))

#         a = np.array(a,dtype=object)
#         b = np.array(b,dtype=object)
#         c = np.array(c,dtype=object)
        
#         if index == 0:
#           data = np.hstack((a,b,c))
#         else:
#           data = np.hstack((data,b,c))
     

#     except:
#         print("Error")

#     index += 1

# data = np.array2string(data, separator= ', ')

# print(data)
# print('\n')

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
# ------------------------------------------------------------------------ #