# demo-django-resistance-app
Let's resist the rails empire with django 2! A mini workshop to introduce the django web framework.


# How to start

```
git clone
virtualenv -p python3 demoenv
. demoenv/bin/activate
pip install -r requirements.txt
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
