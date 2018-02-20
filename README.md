# demo-django-resistance-app

[![Join the chat at https://gitter.im/demo-django-resistance-app/Lobby](https://badges.gitter.im/demo-django-resistance-app/Lobby.svg)](https://gitter.im/demo-django-resistance-app/Lobby?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)
Let's resist the rails empire with django 2! A mini workshop to introduce the django web framework.

# How to start

Vous trouverez ci-dessous les quelques commandes qui vous permettront de commencer à travailler sur le workshop. #DockerSurcoté

```
git clone https://github.com/HE-Arc/demo-django-resistance-app.git .
git checkout todo-resistance-app
virtualenv -p python3 demoenv
. demoenv/bin/activate
pip install -r requirements.txt
cd resistanceproject
python manage.py runserver
```

Si vous voyez du rouge après la dernière commande (un truc de migrations) et une erreur en atteignant `localhost:8000`... C'est que c'est tout bon !

## Méthodologie

L'app est pré-existante. Il faudra remplir les trous (TODOs) pour la rendre fonctionnelle (eeeasy!).

On part de TODO-0-X jusqu'à TODO-7-X, avec à chaque étape quelques lignes à taper.

On fait une recherche dans l'arborescence (Ctrl+Shift+F avec Atom p.ex) et on recherche les TODOS un à un.

Les réponses se trouvent dans le README sur la branche `todo-resistance-app` mais **c'est de la triche de regarder**. C'est seulement en cas d'urgence (je vous vois).

## There's no magic

Avant de vous mettre à disposition les fichiers du repo, voilà les quelques commandes effectuées pour générer l'arborescence. C'est presque rien et c'est fait très vite.

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
