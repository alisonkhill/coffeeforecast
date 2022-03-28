# Import necessary packages
import requests
import datetime
import matplotlib.pyplot as plt


# Obtain zip code from user and validate that it's 5 digits
def get_zip():
    while True:
        zip_code = input('What is your zip code?\n')
        if len(zip_code) == 5 and zip_code.isdigit():
            break
        else:
            print('Your zip code must be 5 digits.')
            continue
    return zip_code        


# Obtain positionstack API Key from user, output coordinates
def get_location():
    while True:
        try:
            location_api_key = input('Please enter a positionstack API Key. You can request one for free at https://positionstack.com/signup/free \n')
            LOCATION_URL = 'http://api.positionstack.com/v1/forward?access_key='+location_api_key+'&query='+user_zip+'&country=US&output=json'
            location_request = requests.get(LOCATION_URL)
            location_json = location_request.json()
            lat = str(location_json.get('data')[0].get('latitude'))
            lon = str(location_json.get('data')[0].get('longitude'))
        except TypeError:
            print('Your positionstack API Key was unsuccessful.')
            continue
        else:
            break
    return lat, lon


# Obtain OpenWeatherMap API key from user, input coordinates, output temperature and conditions
def get_weather():
    while True:
        try:
            weather_api_key = input('Please enter an OpenWeatherMap API Key. You can request one for free at https://home.openweathermap.org/users/sign_up \n')
            WEATHER_URL = 'https://api.openweathermap.org/data/2.5/onecall?&lat='+coordinates[0]+'&lon='+coordinates[1]+'&exclude=minutely,hourly&appid='+weather_api_key+'&units=imperial'
            weather_request = requests.get(WEATHER_URL)
            weather_json = weather_request.json()
            offset = str(weather_json.get('daily')[0].get('sunrise'))
        except TypeError:
            print('Your OpenWeatherMap API Key was unsuccessful.')
            continue
        else:
            break
    return weather_json


# Create lists of variables for graph
def get_forecast():
    # Create empty lists for dates, relative temperatures, and conditions
    days = []
    rel_temps_F = []
    rel_temps_C = []
    conditions = []        
    # Loop through the next 7 days and populate lists
    for x in range(0,7):
        # Get date from json
        dt = weather.get('daily')[x].get('dt')
        # Convert date to strftime
        days.append(datetime.datetime.utcfromtimestamp(dt).strftime('%a %d %b'))
        rel_temps_F.append(round(weather.get('daily')[x].get('feels_like').get('day')))
        rel_temps_C.append(round((rel_temps_F[x] - 32) * (5/9)))
        conditions.append(weather.get('daily')[x].get('weather')[0].get('main'))
    return days, rel_temps_F, rel_temps_C, conditions


# Recommend Hot or Iced based on relative temperature and conditions
def recommendation():
    recs = []
    for x in range(0,7):
        if forecast[1][x] < 50:
            recs.append('Hot')
        elif 60 > forecast[1][x] > 50:
            if forecast[3][x] == 'Clear':
                recs.append('Iced')
            else:
                recs.append('Hot')
        else:
            recs.append('Iced')
    return recs


# Assign conditions to colors for bar graph display
def assign_colors(): 
    conditions_colors = []
    for condition in forecast[3]:
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
    return(conditions_colors)


# Plot bar chart with table data below
def make_chart():
    plt.figure(figsize=(10,10))
    plt.bar(forecast[0], forecast[1], color = colors, edgecolor = 'black')
    plt.table(cellText=[forecast[2], forecast[3], coffees], rowLabels=['Feels Like, Deg (C)','Conditions', 'Coffee Order'], cellLoc='center',bbox=[0.0,-0.45,1,0.28])
    plt.title('Coffee Forecast')
    plt.ylabel('Feels Like, Deg (F)')
    plt.xticks(rotation=45)
    plt.subplots_adjust(left=0.3, bottom=0.4)
    plt.show()


# Calling functions
print('Greetings, coffee drinker!')
user_zip = get_zip()
coordinates = get_location()
weather = get_weather()
forecast = get_forecast()
coffees = recommendation()
colors = assign_colors()
chart = make_chart()
print('Please caffeinate responsibly.\n')




