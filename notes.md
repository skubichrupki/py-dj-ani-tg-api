1. create virtual environment in repo

```
python -m venv .venv
source ./venv/bin/activate
- select interpreter
/Users/skubi/Downloads/git/py-dj-ani-tg-api/.venv/bin/python3
```

2. install django and other packages in venv

```
python3 -m pip install django
(upgrade pip in venv)
python3 -m pip install requests
```

3. create django project in current dir

```
django-admin (list options)
django-admin help startproject
django-admin startproject ani_tg_project .
```

4. run/shutdown dev server

```
python manage.py runserver
pkill -f runserver
```

5. add apis application to project

- app must be in same dir as manage.py

```
python manage.py startapp apis
```

6. add app to settings.json / INSTALLED_APPS

```py
INSTALLED_APPS = ['apis.apps.ApisConfig']
```

7. init project (make first migrations)

```py
python3 manage.py makemigrations
python3 manage.py migrate
```

8. create an app view (html site)

in app:
- add function to views.py
- create apps/templates/index.html
- add path to urlpatterns list in urls.py (create urls.py) (path to site)
```py
path(route='index', view=views.index, name='index')
```
in project;
- add path to urlpatterns list in urls.py (path to app)
```py
path(route='apis/', view=include('apis.urls'))
```

9. create an API request script with class and requests
- animechan_api.py

10. run database (postgresql)

install postgres
```
brew install postgres
brew services start postgres@14
```
install django's postgres adapter in venv
```
python3 -m pip install psycopg2-binary
```

add database to settings.py / DATABASES in project
```py
    'default': {
    'ENGINE': 'django.db.backends.postgresql',
    'NAME': 'skubi',
    'USER': 'postgres',
    'PASSWORD': '',
    'HOST': '127.0.0.1',
    'PORT': '5432'
    }
```

11. model database in app/models.py

10. upload quote to postgres databse (TO DO)

- add connection to postgres in SETTINGS - done
- add adapter psychopg2-binary - done
- create model in apps.models.py - done
- makemigrations and migrate model to db - done
- add create/insert in api view - done
- show data in index view - done