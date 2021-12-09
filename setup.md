
# Instructions for starting the project

## 1) Install poetry and activate venv

```
$ pip install poetry
$ poetry install
$ poetry shell
```
## 2) Then install the dependencies:(if you dont use poetry)

```
$ pip install -r requirements.txt
$ pip install -r dev.txt
```
## 3) Create DB

```
$ python manage.py migrate
$ python manage.py loaddata db.json
```

## 4) Start server

```
$ python manage.py runserver
```
## 5) Read README.md 
_____
# Admin (if you need)

## 1) To enter the admin panel, you first need to create a superuser

```
$ python manage.py createsuperuser
```

## 2) Then log in [here](http://127.0.0.1:8000/admin)