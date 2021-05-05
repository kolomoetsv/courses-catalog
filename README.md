## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)

## General info
This project is simple website catalog with a list of courses, created with Django and Bootstrap.
	
## Technologies
Project is created with:
* Python 3.8
* Django 3.2
* SQLite
* Bootstrap 4
	
## Setup
To run this project:

1. clone the project
```
git clone https://github.com/kolomoetsv/courses-catalog.git
```
2. Create and start a a virtual environment
```
virtualenv env --no-site-packages
source env/bin/activate
```
3. Install the project dependencies

4. Then run
```
python manage.py migrate
```
5. Create admin account
```
python manage.py createsuperuser
```
6. Make migrations for the app
```
python manage.py makemigrations ig_miner_app
python manage.py migrate
```
7. To start the development server
```
python manage.py runserver
```
and open localhost:8000 on your browser to view the app.
