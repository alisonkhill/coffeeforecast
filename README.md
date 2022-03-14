### Coffee Forecast

## Summary
This repo is intended to fulfill the project requirements for the Code Louisville Data Analysis 1 Class.

This program provides a user with their "Coffee Forecast" for the next 8 days based on their zip code. The Coffee Forecast recommends whether to have iced coffee or hot coffee based on their local temperature and conditions. 

First, the user inputs their zip code. The positionstack API is then used to convert the zip code into a latitude and longitude. The latitude and longitude are then used to gather the temperature (feels like) and conditions (clear, rain, etc.) using the Open Weather Map API. This data is compared to pre-defined metrics to determine whether iced or hot coffee is suitable.

## Code Louisville Requirements