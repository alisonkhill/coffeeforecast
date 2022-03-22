# Coffee Forecast

## Summary
This repo is intended to fulfill the project requirements for the Code Louisville Data Analysis 1 Class.

This program provides a user with their "Coffee Forecast" for the week based on their zip code. The Coffee Forecast recommends whether to have iced coffee or hot coffee based on their local temperature and conditions.

First, the user inputs their zip code. The positionstack API is then used to convert the zip code into a latitude and longitude. The latitude and longitude are used to gather the relative temperature (feels like) and conditions (clear, rain, etc.) using the Open Weather Map API. This data is compared to pre-defined metrics in a recommendation function to determine whether iced or hot coffee is suitable.

## Packages & Modules
Coffee Forecast uses requests, json, datetime, and pandas.

## Setup Instructions
There are two version of the coffeeforecast program in this repo:
- [coffeeforecast_api.py](coffeeforecast_api.py) requires use of two API Keys. These are free and can be requested at the following links:
    - [positionstack](https://positionstack.com/signup/free)
    - [OpenWeatherMap](https://home.openweathermap.org/users/sign_up)
- [coffeeforecast_json.py](coffeeforecast_json.py) provides a way to test the program without using an API. 2 sample json files representing output from the APIs are included in the repo to use instead.
    - These are static and therefore used fixed locations and weather for Louisville, KY 40206.
    - The coordinates are printed as well as the coffee forecast to demonstrate the functionality of the program to access both location and weather data.

To run this program, first create a virtual environment with the command: `python3 -m venv virtual-env`

After creating the virtual environment, activate it on Mac/Linux with the command: `source virtual-env/bin/activate`

For Windows: `virtual-env\Scripts\activate.bat`

After activating the virtual environment, install packages in the requirements.txt file using: `python -m pip install -r requirements.txt`

Finally, run: `python coffeeforecast_api.py` if you have API keys, or `python coffeeforecast_json.py` if not.

## Code Louisville Requirements

- [x] The project is uploaded to your GitHub repository and shows at minimum 5 separate commits.
- [x] Gitignore should be used to keep any secrets/passwords used to access APIs / data sources out of the Github repository

> The project includes a README file that explains the following:
- [x] A one-paragraph or longer description of what your project is about.
- [x] Relevant packages that need to be installed to run the project.
- [x] Which 3+ features you have included from the below lists to meet the requirements
- [x] Any special instructions are required for the reviewer to run your project. (For example: “run python main.py” from the command line)

- [x] The project should implement a simple data analysis by reading data, performing calculations on the data, and displaying the results.

### Choose at least 1 item from each category on the Features List below and implement them in your project

#### Category 1: Python Programming Basics
> Create a dictionary or list, populate it with several values, retrieve at least one value, and use it in your program.

A dictionary of lists called "forecast" is created and populated with data from the Open Weather Map API. Each date is a key, with the corresponding value being a list containing relative temperature, conditions, and coffee recommendation.

#### Category 2: Utilize External Data:
> Connect to an external/3rd party API and read data into your app

Data from two APIs are used: positionstack and Open Weather Map

#### Category 3: Data Display
> Display data in tabular form

The output of the program is a table showing the relative temperature, conditions, and coffee order recommended for each date.

#### Category 4: Best Practices
> The program should utilize a virtual environment and document library dependencies in a requirements.txt file

See requirements.txt file in repo.

#### Stretch Features (optional):
> Use pandas, matplotlib, and/or numpy to perform a data analysis project. Ingest 2 or more pieces of data, analyze that data in some manner, and display a new result to a graph, chart, or other display.

Pandas is used to display the final table.
