# Movie Django App
There are 2 apps in the service: Authentication and Films

## Description
Authentication which allows a user to create and update a user
The following endpoints are exposed:
- route `/auth/profile/` method=`GET|POST|PUT|DELETE`. In case of `POST|PUT` the fields required are the following: 
email
username
first_name
last_name
password
- route `/auth/login/` method=`POST` the fields required are the following: 
username (refers to Email)
password
Returns a token necessary for using the other APIs

note: The data must be sent as form-data

Films which allows an authenticated user to consult movies and persons available in the catalog
- route `/movies/` method=`GET`
Returns a list of movies
- route `/movies?title=title` method=`GET`
Returns a list of movies which contains the title specified
- route `/movies?genre=genre` method=`GET`
Returns a list of movies which contains the genre specified
- route `/persons/` method=`GET`
Returns a list of actors and directors
- route `/persons?name=name` method=`GET`
Returns a list of actors and directors which contains the name specified

note: every endpoint requires a header `Authorization` : `Token `token`

## Prerequisited and Installation
- Install python 3
- Create virtual environment `virtualenv -p python3 venv`
- Run `pip install requirements.txt`
- Install postgress
- Load the schemas and data to postgres (copy schema files to postgres instance)

## Run
- Connect to postgres instance (Change settings file)
- Run in cli `python manage.py makemigrations`
- Run in cli `python manage.py migrate`
- Run in cli `python manage.py runserver`
