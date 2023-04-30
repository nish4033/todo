# TODO

Behold My Awesome Project!

[![Built with Cookiecutter Django](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?logo=cookiecutter)](https://github.com/cookiecutter/cookiecutter-django/)
[![Black code style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

## Settings

Moved to [settings](http://cookiecutter-django.readthedocs.io/en/latest/settings.html).

## Basic Commands
cd <path-to-folder>
python3 -m virtualenv venv
source venv/bin/activate
pip install -r requirements/local.txt
create a mysql db
 create an .env file and add these variables
```
DB_NAME=todo_db
DB_USER=root
DB_PASSWORD=
DB_HOST=localhost
JWT_SECRET_KEY=
SALT=
```
python manage.py runserver

## Deployment
python3 -m virtualenv venv

## check todo.json for postman collection to use the apis
### Docker

