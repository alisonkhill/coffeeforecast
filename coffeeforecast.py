# Import necessary packages
import requests
import pandas as pd
import datetime
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# Get zip code from user and validate that it's 5 digits
def get_zip():
    while True:
        global zip_code
        zip_code = input('Greetings, coffee drinker!\nWhat is your zip code?\n')
        if len(zip_code) == 5:
            break
        else:
            print('Your zip code must be 5 digits.')
            continue
    return zip_code        


# Validate API Key and get lat and lon for weather URL
def get_location():
    while True:
        try:
            location_api_key = input('Please enter a positionstack API Key. You can request one for free at https://positionstack.com/signup/free \n')
            LOCATION_URL = 'http://api.positionstack.com/v1/forward?access_key='+location_api_key+'&query='+zip_code+'&country=US&output=json'
            location_request = requests.get(LOCATION_URL)
            location_json = location_request.json()
            global lat
            lat = str(location_json.get('data')[0].get('latitude'))
            global lon
            lon = str(location_json.get('data')[0].get('longitude'))
        except TypeError:
            print('Your positionstack API Key was unsuccessful.')
            continue
        else:
            break
    return lat, lon

# Validate OpenWeatherMap API key and get temperature and conditions from open weather map API using latitude and longitude
def get_weather():
    while True:
        try:
            weather_api_key = input('Please enter an OpenWeatherMap API Key. You can request one for free at https://home.openweathermap.org/users/sign_up \n')
            WEATHER_URL = 'https://api.openweathermap.org/data/2.5/onecall?&lat='+lat+'&lon='+lon+'&exclude=minutely,hourly&appid='+weather_api_key+'&units=imperial'
            weather_request = requests.get(WEATHER_URL)
            global weather_json
            weather_json = weather_request.json()
            offset = str(weather_json.get('daily')[0].get('sunrise'))
        except TypeError:
            print('Your OpenWeatherMap API Key was unsuccessful.')
            continue
        else:
            break
    return weather_json

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
def get_forecast():
    global forecast
    forecast = {}
    for x in range(0,7):
        # Get date from json
        dt = weather_json.get('daily')[x].get('dt')
        # Convert date to strftime
        day = datetime.datetime.utcfromtimestamp(dt).strftime('%a %d %b')
        # Get Feels Like temperature
        global feels_like
        feels_like = round(weather_json.get('daily')[x].get('feels_like').get('day'))
        # Get conditions
        global conditions
        conditions = weather_json.get('daily')[x].get('weather')[0].get('main')
        # Get recommendation using function defined above
        global rec
        rec = recommendation()
        # Put into dictionary of lists
        forecast[day] = [rec, feels_like, conditions]
    # Output as table using pandas module    
    global df
    df = pd.DataFrame.from_dict(forecast, orient = 'index', columns = ['Coffee Order','Feels Like', 'Conditions'])
    

get_zip()
get_location()
get_weather()
get_forecast()

print('\n Here is your coffee forecast. Please caffeinate responsibly.\n')
print(df)

# Output as bar graph using matplotlib
# First access dates and "feels likes" from forecast dictionary to create lists
keys_list = list(forecast)
coffee_list = []
temp_list = []
conditions_list = []
for key in keys_list:
    coffee_list.append(forecast.get(key)[0])
    temp_list.append(forecast.get(key)[1])
    conditions_list.append(forecast.get(key)[2])

conditions_colors = []
for condition in conditions_list:
    if condition == "Clouds" or condition == 'Fog':
        conditions_colors.append('grey')
    elif condition == 'Clear':
        conditions_colors.append('yellow')
    elif condition == 'Rain' or condition == 'Drizzle' or condition == 'Thunderstorm':
        conditions_colors.append('blue')
    elif condition == 'Snow':
        conditions_colors.append('whitesmoke')
    else:
        conditions_colors.append('black')

# Plot bar chart with dates on the x-axis and "feels likes" on the y

# Define legend colors
clear_patch = mpatches.Patch(color='yellow', label='Clear')
clouds_patch = mpatches.Patch(color = 'grey', label = 'Clouds')
rain_patch = mpatches.Patch(color = 'blue', label = 'Rain')
snow_patch = mpatches.Patch(color = 'whitesmoke', label = 'Snow')
other_patch = mpatches.Patch(color = 'black', label = 'Other')

plt.figure(figsize=(7,9))
plt.bar(keys_list, temp_list, color = conditions_colors, edgecolor = 'black')
plt.title('Coffee Forecast')
plt.xlabel('Date')
plt.xticks(rotation = 35)
plt.ylabel('"Feels Like" (F)')
plt.legend(handles = [clear_patch, clouds_patch, rain_patch, snow_patch, other_patch])
plt.show()
