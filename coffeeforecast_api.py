# Import necessary packages
import requests
import pandas as pd
import datetime

# Get zip code from user
zip = input('Greetings, coffee drinker! What is your zip code?\n')
LOCATION_API_KEY = input('Please enter a positionstack API Key. You can request one for free at https://positionstack.com/signup/free \n')

# Convert zip code to latitude and longitude using positionstack API
LOCATION_URL = 'http://api.positionstack.com/v1/forward?access_key='+LOCATION_API_KEY+'&query='+zip+'&country=US&output=json'
location_request = requests.get(LOCATION_URL)
location_json = location_request.json()
lat = str(location_json.get('data')[0].get('latitude'))
lon = str(location_json.get('data')[0].get('longitude'))

print('Your coordinates are ' + lat + ', ' + lon + '\n')

WEATHER_API_KEY = input('Please enter an OpenWeatherMap API Key. You can request one for free at https://home.openweathermap.org/users/sign_up \n')

# Get temperature and conditions from open weather map API using latitude and longitude
WEATHER_URL = 'https://api.openweathermap.org/data/2.5/onecall?&lat='+lat+'&lon='+lon+'&exclude=minutely,hourly&appid='+WEATHER_API_KEY+'&units=imperial'
weather_request = requests.get(WEATHER_URL)
weather_json = weather_request.json()

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
    day = datetime.datetime.utcfromtimestamp(dt).strftime('%A %d %B %Y')
    # Get Feels Like temperature
    feels_like = round(weather_json.get('daily')[x].get('feels_like').get('day'))
    # Get conditions
    conditions = weather_json.get('daily')[x].get('weather')[0].get('main')
    # Get recommendation using function defined above
    rec = recommendation()
    # Put into dictionary of lists
    forecast[day] = [rec, feels_like, conditions]

# Output as table using pandas module    
df = pd.DataFrame.from_dict(forecast, orient = 'index', columns = ['Coffee Order','Feels Like', 'Conditions'])
print('Here is your coffee forecast. Please caffeinate responsibly.\n')
print(df)