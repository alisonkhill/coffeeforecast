# Coffee Forecast

## Summary
This repo is intended to fulfill the project requirements for the Code Louisville Data Analysis 1 Class.

This program provides a user with their "Coffee Forecast" for the week based on their zip code (United States zip codes only). The Coffee Forecast recommends whether to have iced coffee or hot coffee based on their local temperature and conditions.

First, the user inputs their zip code. The positionstack API is then used to convert the zip code into a latitude and longitude. The latitude and longitude are used to gather the relative temperature (feels like) and conditions (clear, rain, etc.) using the Open Weather Map API. This data is compared to pre-defined metrics in a recommendation function to determine whether iced or hot coffee is suitable.

## Packages & Modules
Coffee Forecast uses requests, datetime, and matplotlib.

## Setup Instructions
1. [coffeeforecast.py](coffeeforecast.py) requires use of two API Keys. These are free and can be requested at the following links:
- [positionstack](https://positionstack.com/signup/free)
- [OpenWeatherMap](https://home.openweathermap.org/users/sign_up)

2. Next, set up a virtual environment:
    - On Mac or Linux:
        - open the Terminal and create a virtual environment with the command `python3 -m venv virtual-env`
        - activate the virtual environment with the command `source virtual-env/bin/activate`
    - On Windows, 
        - open the Command Prompt and create a virtual environment with the command `python -m venv virtual-env`
        - activate the virtual environment with the command `virtual-env\Scripts\activate.bat`

3. Install packages in the requirements.txt file
    - Mac: `python3 -m pip install -r requirements.txt`
    - Windows: `python -m pip install -r requirements.txt`

4. Finally, run `python coffeeforecast.py` and have your API keys handy.

## Future Enhancements
Some ideas to improve this repo in the future include:
- Expanding to include global postal codes instead of just the United States
- Accessing local coffee shops based on the user's zip code and recommending shops and even specific beverage orders.
- Adding a time of day element to recommend decaf or regular coffee.

## Code Louisville Requirements

- [x] The project is uploaded to your GitHub repository and shows at minimum 5 separate commits.
- [x] Gitignore should be used to keep any secrets/passwords used to access APIs / data sources out of the Github repository
- [x] The project includes a README file that explains the following:
    - A one-paragraph or longer description of what your project is about.
    - Relevant packages that need to be installed to run the project.
    - Which 3+ features you have included from the below lists to meet the requirements
    - Any special instructions are required for the reviewer to run your project. (For example: “run python main.py” from the command line)
- [x] The project should implement a simple data analysis by reading data, performing calculations on the data, and displaying the results.

### Choose at least 1 item from each category on the Features List below and implement them in your project

#### Category 1: Python Programming Basics
> Create a dictionary or list, populate it with several values, retrieve at least one value, and use it in your program.

Several lists are created and populated with data from the OpenWeatherMap API, including dates, relative temperatures, conditions, and coffee recommendations.

> Create and call at least 3 functions or methods, at least one of which must return a value that is used somewhere else in your code. To clarify, at least one function should be called in your code, that function should calculate, retrieve, or otherwise set the value of a variable or data structure, return a value to where it was called, and use that value somewhere else in your code

There are six functions in Coffee Forecast, five of which return values that are used in other functions.

#### Category 2: Utilize External Data:
> Connect to an external/3rd party API and read data into your app

Data from two APIs are used: positionstack and OpenWeatherMap

#### Category 3: Data Display
> Display data in tabular form
> Visualize data in a graph, chart, or other visual representation of data.

The output of the program is a figure including a bar graph and a table showing the relative temperature, conditions, and coffee order recommended for each date. The bars are color-coded according to the conditions.

#### Category 4: Best Practices
> The program should utilize a virtual environment and document library dependencies in a requirements.txt file

See requirements.txt file in repo.

#### Stretch Features (optional):
> Use pandas, matplotlib, and/or numpy to perform a data analysis project. Ingest 2 or more pieces of data, analyze that data in some manner, and display a new result to a graph, chart, or other display.

Matplotlib is used to display the forecast figure.
