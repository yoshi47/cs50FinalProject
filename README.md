# Ikuyosan

#### Video Demo: https://youtu.be/TkhGPPXWBkg

You can try the app on [Heroku](https://ikuyosan.herokuapp.com/)

![img.png](https://user-images.githubusercontent.com/64204237/133374267-207abf51-f3e2-4d65-a49c-a0afdf0c3c3d.png)

## About 

This app allows you to get a quick estimate of your trip.
You can easily see how much you need for your trip.

Place names are complemented using autocomplete, but will not be available if the API limit is exceeded.
If this happens, please try to enter the name of the prefecture first.
If this happens, please try to enter the name of the prefecture first, or the name of a place with the same name in a different place than you expected will be used.

## Technologies used

- Flask
- jQuery
- NAVITIME API for Rakuten RapidAPI
- Bootstrap
- Heroku
- Gunicorn

## How to get an estimate

1. user enters information
2. get the address of the starting point and destination
3. get travel route and highway fare
4. add the highway fee and gasoline fee
5. add the cost of accommodation
6. Estimate completed!

## Possible improvements

As all applications this one can also be improved. Possible improvements:

- Make it optional to add things to do on the trip. Theme parks, camping, hot springs, skiing/snowboarding, snorkeling, car rental, etc.
- Hotel prices are flat, so get the price for each search and calculate it.
- Traveling by public transportation
- Change the load screen.
- Support overseas travel
- Use FastAPI for the backend to speed up the process.

