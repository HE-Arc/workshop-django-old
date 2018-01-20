# demo-django-resistance-app
Let's resist the rails empire with django 2! A mini workshop to introduce the django web framework.


# How to start

```
git clone https://github.com/HE-Arc/demo-django-resistance-app.git
git checkout step-{x}
cd demo-django-resistance-app
virtualenv -p python3 demoenv
. demoenv/bin/activate
pip install -r requirements.txt
cd resistanceproject
python manage.py runserver

```

# Additional informations

## What I did to get to step-0

```
virtualenv -p python3 demoenv
. demoenv/bin/activate
pip install Django
django-admin startproject resistanceproject
cd resistanceproject
python manage.py startapp resistanceapp
python manage.py migrate
```
Took something like 30 seconds to get ready to work.


## How to go from step-0 to step-1

```
pip install django-bootstrap4
pip freeze
pip freeze > requirements.txt
```
