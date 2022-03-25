# Import necessary packages
import json
import pandas as pd
import datetime
import matplotlib.pyplot as plt


# Convert zip code to latitude and longitude using positionstack json
with open('location_example.json') as x:
    location_json = json.load(x)
lat = str(location_json.get('data')[0].get('latitude'))
lon = str(location_json.get('data')[0].get('longitude'))


# Get temperature and conditions from open weather map json using latitude and longitude
with open('weather_example.json') as f:
    weather_json = json.load(f)


# Function to recommend Hot or Iced based on relative temperature and conditions
def recommendation():
    if feels_like < 50:
        return('Hot')
    elif 60 > feels_like > 50:
        if conditions == 'Clear':
            return('Iced')
        else:
            return('Hot')
    else:
        return('Iced')


# Create dictionary of weather and recommendations mapped to each date
forecast = {}
for x in range(0,7):
    # Get date from json
    dt = weather_json.get('daily')[x].get('dt')
    # Convert date to strftime
    day = datetime.datetime.utcfromtimestamp(dt).strftime('%a %d %b')
    # Get Feels Like temperature
    feels_like = round(weather_json.get('daily')[x].get('feels_like').get('day'))
    # Get conditions
    conditions = weather_json.get('daily')[x].get('weather')[0].get('main')
    # Get recommendation by calling above function
    rec = recommendation()
    # Put into dictionary of lists
    forecast[day] = [rec, feels_like, conditions]


# Output as table using pandas module to create dataframe    
df = pd.DataFrame.from_dict(forecast, orient = 'index', columns = ['Coffee Order', 'Feels Like', 'Conditions'])
df.style
print('The coffee forecast for coordinates ' + lat + ', ' + lon + ' is:')
print(df)
print('Please caffeinate responsibly.')


# Output as bar graph using matplotlib
# First access dates and "feels likes" from forecast dictionary to create lists
temps = {}
for key, val in forecast.items():
    temps[key] = val[1]   
dates = list(temps.keys())
temps_F = list(temps.values())

# Plot bar chart with dates on the x-axis and "feels likes" on the y
plt.bar(dates, temps_F)
plt.title('Coffee Forecast')
plt.xlabel('Date')
plt.ylabel('"Feels Like" (F)')
plt.show()