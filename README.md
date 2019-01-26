[![Build Status](https://travis-ci.org/saidjillo/game-workshop.svg?branch=master)](https://travis-ci.org/saidjillo/game-workshop)

# Django -> Game Workshop

An online platform where people can create accounts and manages games and favorite lists of games

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them

```
# You can get a copy of this project by:
   #  -- downloading the repository as a zip file
   #  -- cloning the project into your local repository
   # navigate into the project folder and run 

   pip install -r requirements.txt

   # this installs all the required dependecies
```

### Installing

Installing the project is easy

1. create a virtual environment
   - navigate into the project directory and run 
```
 virtualenv venv
```
to create a virtual environment

2. Apply migrations
   - make sure to apply all migrations using the following command
```
python manage.py migrate
python manage.py makemigrations
python manage.py migrate
```

3. finally you test the program by running ```python manage.py runserver```

## Running the tests

To run the automated tests for this system run the following  command in the same directory as ```manage.py```
```
python manage.py test
````


### Test coverage
these tests covers the following areas
     1. models
     2. views


## Deployment

The project is currently hosted at * [saidjillo.pythonanywhere.com](http://www.saidjillo.pythonanywhere.com/)



## Live demo
  - games --> [saidjillo.pythonanywhere.com](http://www.saidjillo.pythonanywhere.com/)


## Authors

 

* **Said Umuru Jillo** - *Initial work* - [saidjillo.pythonanywhere.com](http://www.saidjillo.pythonanywhere.com/)



## project preview
![app screenshot](https://raw.githubusercontent.com/saidjillo/game-workshop/master/screencapture-saidjillo-pythonanywhere-2019-01-22-15_10_42.png)



