# Ikuyosan

### Video Demo

#### There is a demo video on You Tube that explains how to use it. Please take a look.

#### Here's the link.

- https://youtu.be/TkhGPPXWBkg

### Try this app

#### You can try the app on [Heroku](https://ikuyosan.herokuapp.com/)

![img.png](https://user-images.githubusercontent.com/64204237/133374267-207abf51-f3e2-4d65-a49c-a0afdf0c3c3d.png)

## About

#### This app allows you to get a quick estimate of your trip. You can easily see how much you need for your trip.

#### Place names are complemented using autocomplete, but will not be available if the API limit is exceeded.
#### If this happens, please try to enter the name of the prefecture first.
#### If this happens, please try to enter the name of the prefecture first, or the name of a place with the same name in a different place than you expected will be used.

##### sorry
#### I don't think so, but if the API requests reach the limit, this app will not work. Please wait until the next month.

## Technologies used

- ~~Flask~~
- Django
- jQuery
- NAVITIME API for Rakuten RapidAPI
- Bootstrap
- Heroku
- Gunicorn

## How to get an estimate

#### This app calculates your total spending every time!

1. user enters information
2. get the address of the starting point and destination
3. get travel route and highway fare
4. add the highway fee and gasoline fee
5. add the cost of accommodation
6. Estimate completed!

## Possible improvements

#### As all applications this one can also be improved. Possible improvements:

- [ ] Make it optional to add things to do on the trip. Theme parks, camping, hot springs, skiing/snowboarding, snorkeling,
  car rental, etc.
- [ ] Hotel prices are flat, so get the price for each search and calculate it.
- [ ] Traveling by public transportation
- [ ] Change the load screen.
- [ ] Support overseas travel
- [x] Adding a Database

## What was difficult.

#### I thought it would be difficult to get information using APIs, but I found out that it is not difficult if you follow the steps.
Implementing the autocomplete function was the most technically difficult, since it was my first time to use ajax for communication, and it took a lot of time to apply it.
I think this app could be improved, so I would like to add more functions little by little.