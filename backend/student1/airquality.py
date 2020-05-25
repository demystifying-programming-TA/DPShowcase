# ------------------------------------------------------------------------ #
# Initialization
# ------------------------------------------------------------------------ #

# Load dependencies
# ---------------------------------------------#
import pandas as pd
import geopy as gp
import requests
# ------------------------------------------------------------------------ #
# Define Functions
# ------------------------------------------------------------------------ #

# location_mobility_data
# ----------------------------
def location_mobility_data(longitude, latitude,radius):

    # Load the data
    #print(str(longitude)+","+str(latitude))
    parameters = {"coordinates": str(latitude)+","+str(longitude),
     "radius":radius,
     "date_from": "2020-02-01",
     "date_to": "2020-04-30",
     "parameter": "pm25",
     "limit":10000
     }

    aq_data_req = requests.get("https://api.openaq.org/v1/measurements", params = parameters)
    aq_data = aq_data_req.json()
    

    dates = []
    values = []
    valuesAvg =[]
    den = 0 
    valuesSum=0


    for i in range(10,82):
        if i < 21:
            num = '2020-02-{:>02d}'.format(i)
        elif i < 52:
            num = '2020-03-{:>02d}'.format(i-20)
        else:
            num = '2020-04-{:>02d}'.format(i-51)

        try:
            dictItem = next((item for item in aq_data['results'] if
                    item['date']['utc'][:10] == num),None)

            dates.append(dictItem['date']['utc'][:10])
            values.append(dictItem['value'])
            
        except:
            dates.append([])
            values.append([])

        for j in range(1,10):
            try:
                valuesSum += values[i-j-10]
                den +=1
            except:
                valuesSum += 0

        try:

            valuesAvg.append(round(valuesSum/den,2))
        except:
            valuesAvg.append([])
        
        valuesSum = 0
        den = 0


    location = (dictItem["location"])


    # Extract data for country
   
    # Reverse geocode (longitude, latitude > country)
    locator      = gp.geocoders.Nominatim(user_agent="myGeocoder")       
    coordinates  = str(latitude) + ", " + str(longitude)    
    geocode_data = locator.reverse(coordinates)             
    country      = geocode_data.raw['address']['country']

    #print(geocode_data)
    #print(aq_data)

    # Extract data for walking & calculate change in # of walking calls
    
    # Extract data for driving & calculate change in # of driving calls
   
    # Return the results
    return([location,dates, values, valuesAvg])

