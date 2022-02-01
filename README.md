# Django Exercises
Django Exercises!

## How to Run:
You can use Docker or run through your own environment.

**🐋 Using Docker:**

(Unavailable for now)
```sh
$ docker build -t dj_exercises:latest .
$ docker run -it dj_exercises:latest
```

**💻 Using Your Local Environment:**

First, create and activate a virtual environment:
```sh
$ python3 -m venv .venv
$ . .venv/bin/activate
```
Install dependencies:
```sh
$ pip install -U pip -r requirements.txt
```
*Run tests:*
```sh
$ python manage.py test
$ # or python manage.py test some_app
```
*Run app:*
```sh
$ python manage.py runserver
```


**🚀 List of Exercises**
 1. Bookstore CRUD API with DRF:

    | Details                 | Method |
    | ----------------------- | ------ |
    | Create a Book           | POST   |
    | Read all the Books      | GET    |
    | Update a Book           | PUT    |
    | Delete a Book           | DELETE |
 
 2. Use HTMX with the last one exercise;
 3. Test Database;
 4. Reuse Django Admin;
 5. Authorization;
 6. Make an ETL with the Bookstore;
