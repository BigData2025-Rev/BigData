# MongoDB Activity Week 3 - Weather Data

## Goal
- Practice MongoDB queries

## Steps

- Import [rdu-weather-history.json](./rdu-weather-history.json) into a mongodb collection titled "weather". You can do this using MongoDBCompass.
    - The schema is as follows
        ```
        {
            date : The date of the recorded weather,
            tmin : Minimum temperature,
            tmax : Maximum temperature,
            prcp : Precipitation measured in inches,
            snow : Snowfall measured in inches,
            snwd : Snow depth measured in inches,
            awnd : Average wind speed
        }
        ```
- Write queries to complete the following tasks:

    1) Return the document that represents the weather data for October 23, 2017.
    2) Return the documents from July of 2018 sorted by tmax.
    3) What is the most amount of precipitation in a single day?
    4) What was the hottest day in 2019?
    5) How much total precipitation was there in 2017?
    6) What was the coldest day when it snowed?


