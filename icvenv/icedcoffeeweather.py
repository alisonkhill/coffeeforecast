# Import necessary packages
import requests

# Get zip code from user
zip = input("What is your zip code?\n")

# Get latitude and longitude from zip code using positionstack API
location_api_key = 'e4c7ae4d85a39faf63881294a9bbc35d'
location_url = 'http://api.positionstack.com/v1/forward?access_key='+location_api_key+'&query='+zip+'&country=US&output=json'

location_request = requests.get(location_url)
location_json = location_request.json()
lat = str(location_json.get('data')[0].get('latitude'))
lon = str(location_json.get('data')[0].get('longitude'))

weather_api_key = '67da29cb91129f1a68c1c06c1be92daa'
weather_url = "https://api.openweathermap.org/data/2.5/onecall?&lat="+lat+"&lon="+lon+"&exclude=minutely,hourly&appid="+weather_api_key+"&units=imperial"

weather_request = requests.get(weather_url)
weather_json = weather_request.json()

# Get temperature and conditions using lat and lon from open weather map API

feels_like = round(weather_json.get("current").get("feels_like"))
conditions = weather_json.get("current").get("weather")[0].get("main")

# Report coffee recommendation based on temperature and conditions
def todays_coffee_forecast():
    if feels_like < 50:
        print("You should have hot coffee today")
    elif 60 > feels_like > 50:
        if conditions == "Clear":
            print("Get yourself an iced coffee today!")
        else:
            print("You should have hot coffee today!")
    else:
        print("Get yourself an iced coffee today")

todays_coffee_forecast()