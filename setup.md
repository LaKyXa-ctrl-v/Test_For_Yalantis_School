
# Instructions for starting the project

## 1)Install poetry and activate venv

```
$ pip install poetry
$ poetry install
$ poetry shell
```
## Then install the dependencies:(if you dont use poetry)

```
$ pip install -r requirements.txt
```
## Create DB

```
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py loaddata db.json

```

## Once pip has finished downloading the dependencies:

```
$ python manage.py runserver
```

# Admin (if you need)

## 1)To enter the admin panel, you first need to create a superuser

```
$ python manage.py createsuperuser
```

## 2)Then log in [here](http://127.0.0.1:8000/admin)