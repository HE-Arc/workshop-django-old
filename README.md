# Introduction

Ce Workshop Django est donné aux étudiants de 3ème année à la HE-Arc dans le cadre du cours de développement web.

L'objectif de ce workshop est de transmettre aux étudiants les bases et les bonnes pratiques de la création d'un projet web avec le Framework Django. Ce workshop a également pour but de fournir un point de départ aux étudiants afin de leur permettre de créer leur projet de semestre.

Les prochaines étapes permettent de mettre en place l'environnement de développement et de suivre le workshop dans son intégralité.

# Explication des branches

Branches générales

- master : la branche contenant la version du README le plus à jour
- start : la branche contenant le code de départ du workshop Django ainsi que les réponses aux TODOs
- end : la branche contenant le code solution du workshop Django (mais c'est de la triche)

Branches par années

- xxxx-start : la branche contenant le code de départ du workshop Django, réalisé avec les étudiants de l'année xxxx
- xxxx-end : la branche contenant le code solution du workshop Django, réalisé avec les étudiants de l'année xxxx

# Prérequis

## Python

Version >= 3.6  
Dépendance provenant du site officiel de Django pour la version utilisé dans ce workshop : https://docs.djangoproject.com/en/3.2/releases/3.2/#python-compatibility

> Le workshop a été testé avec la version 3.8.10 de Python

- Windows

```
python --version
```

- Linux

```
python3 --version
```

## pip

> Le workshop a été testé avec la version 21.3 de pip

- Windows

```
pip --version
```

- Linux

```
pip3 --version
```

pip peut être mit à niveau avec :

```
python -m pip install --upgrade pip
```

# Installation et configuration

Vous trouverez ci-dessous les quelques commandes qui vous permettront de commencer à travailler sur le workshop.

1. Cloner le répo Github du workshop, vous connaissez c'est easy ;)

> SSH recommandé

```
git clone git@github.com:HE-Arc/workshop-django.git
cd workshop-django
git checkout start
```

2. Créer un environnement virtuel (= virtual environment = venv), c'est très important !

Le gestionnaire de paquet en Python s'appelle pip. La technique de base consiste à créer un fichier nommé requiements.txt dans lequel nous allons pouvoir lister toutes les bibliothèques (dépendances) dont notre projet a besoin pour fonctionner correctement.

Par défaut pip installe toutes les bibliothèques globalement sur l'ordinateur, ce qui pourrait paraitre comme une bonne idée à la base car si nous avons un autre projet qui nécessite toutes ou certaines mêmes bibliothèques, les bibliothèques en question seront déjà installées.

Mais en réfléchissement un peu on s'aperçoit très vite que c'est une très mauvaise idée. Certaines bibliothèques pourraient ne pas être compatibles ce qui pourrait rapidement devenir difficile à gérer.

Le mieux est donc de séparer toutes les bibliothèques de tous les projets quitte à devoir réinstaller dans certain cas la même version de certaines d'entre elles.

Pour ce faire nous allons utiliser les environnements virtuels qui nous permettent d'isoler un environnement afin de le séparer de celui de base et des autres que nous allons créer pour d'autres projets.

Il existe plusieurs bibliothèques qui permettent toutes de créer des environnements virtuels, vous pouvez utiliser celui que vous souhaitez. Personnellement j'utilise celui disponible directement avec Python.

Vous devez le créer une fois au début et/ou à chaque fois que vous clonez le projet. Ensuite une fois qu'il est créé pour la première fois vous n'aurez plus qu'à l'activer. Attention il ne faut pas oublier de le réactiver. Vous pouvez checker que vous avez bien l'extension VSCode "Python" (sinon installez là, elle nous sera utile par la suite).

**IMPORTANT** : l'environnement virtuel ne doit JAMAIS être push ! (Le fichier créé lors de la création d'un nouvel environnement virtuel)
**Important** : l'environnement virtuel peut être construit de manière légèrement différente en fonction de l'OS, de l'environnement virtuel utilisé ou pour d'autre raisons. Contrôlez l'architecture des dossiers de votre venv si vous avez des soucis à exécuter l'une ou l'autre des commandes, cela pourrait venir de cela.

- Windows

```
python -m venv .venv
source .venv/Scripts/activate
```

- Linux

```
python3 -m venv .venv
source .venv/bin/activate
```

3. Installer les dépendances dans le venv.

Il existe des débats sur le net au sujet d'une meilleure utilisation de ce fichier.  
Dans ce workshop et dans le projet que vous réaliserez lors de ce cours (projet de petite taille), le fichier requirements.txt est tout à fait adapté.  
Mais si vous souhaitez creuser un peu, des techniques plus avancées existent et vous pouvez checker pipenv (https://pipenv-fork.readthedocs.io/en/latest/basics.html) ou encore poetry (https://python-poetry.org/)

- Windows

```
pip install -r requirements.txt
```

- Linux

```
pip3 install -r requirements.txt
```

4. Démarrer le serveur de dev

Il est possible de structurer son projet différemment, la structure que nous allons utilisez est celle proposée dans Django par défaut. Une fois que vous aurez compris et que vous serez à l'aise n'hésitez pas à chercher comment l'améliorer et l'adapter au mieux pour votre projet.

- Windows

```
cd resistanceproject
python manage.py runserver
```

- Linux

```
cd resistanceproject
python3 manage.py runserver
```

Si vous voyez une image d'espace en atteignant `localhost:8000`... C'est que c'est tout bon !

---

**Prêt pour le workshop !**

Si vous êtes arrivés jusqu'ici, vous êtes prêt pour le workshop.  
La suite vous sera utile lorsque vous devrez créer votre propre projet pour le semestre.

---

# Méthodologie - Comment va se dérouler le workshop ?

L'app est pré-existante. Il faudra remplir les trous (TODOs) pour la rendre fonctionnelle (eeeasy!).

On part de TODO-0-0 jusqu'à TODO-X-Y, avec à chaque étape quelques lignes à taper.

On fait une recherche dans l'arborescence (Ctrl+Shift+F avec VSCode p.ex) et on recherche les TODOs un à un.

Les réponses se trouvent dans le README sur la branche `start` mais **c'est de la triche de regarder**. C'est seulement en cas d'urgence (je vous vois).

# Initialiser un nouveau projet Django de zéro

Ici vous avez un repo avec un projet déjà existant, en réalité c'est juste pour nous faire gagner un peu de temps, mais c'est extrêmement simple à reproduire. Voici donc les premières étapes que vous devrez suivre afin de créer un nouveau projet de zéro (Si ce n'était pas assez clair, les étapes qui vont suivre ne doivent PAS être effectué pour ce workshop, c'est à faire si vous commencez un nouveau projet) :

1. Créer un dossier et déplacez-vous y.

2. S'assurer d'avoir la bonne version de python et de pip pour la version de Django que vous souhaitez utiliser

3. Créer un environnement virtuel (venv)

> **Important** : pour l'environnement virtuel la hiérarchie du projet peut être légèrement différente en fonction de l'OS ou autres. Contrôlez donc l'architecture des dossiers du venv.)

- Windows

```
python -m venv .venv
source .venv/Scripts/activate
```

- Linux

```
python3 -m venv .venv
source .venv/bin/activate
```

4. Installer Django

- Windows

```
pip install Django
```

- Linux

```
pip3 install Django
```

5. Créer le projet Django et déplacez-vous-y

> - Modèle
>
> _(<project_name> : à remplacer par le nom du projet, dans notre cas "resistanceproject", qui n'est pas forcément un bon choix de nom)_
>
> ```
> django-admin startproject <project_name>
> cd <project_name>
> ```

```
django-admin startproject resistanceproject
cd resistanceproject
```

6. Créer votre première app et démarrez les migrations de base

Ici le nom des apps et des projets ont été choisi pour être correspondre au workshop, mais vous pouvez nommer votre projet et vos apps en fonction de votre projet évidemment.

> - Modèle
>
> (<app_name> : à remplacer par le nom de l'app et postfixer avec "app", dans notre cas <app_name> = "resistance" et avec le postfixe cela donne donc : "resistanceapp". Ce n'est pas forcément un bon choix de nom, essayez d'être plus précis dans le choix de vos noms, éviter les noms trop générique)\*
>
> ```
> python manage.py startapp <app_name>app
> python manage.py migrate
> ```

- Windows

```
python manage.py startapp resistanceapp
python manage.py migrate
```

- Linux

```
python3 manage.py startapp resistanceapp
python3 manage.py migrate
```

---

# Q&A

## Séparer le fichiers views.py pour plus de clarté

**Q: @PedroEmanuelCosta**

Est-ce qu’en suite dans le fichier views.py on regroupe tous les contrôleurs de ces modèles ou il est plutôt recommandé de faire plusieurs fichiers séparés plutôt du style à la Laravel ?

**A: @Ishydo**

Si votre projet web de deuxième semestre est qualifiable d'ambitieux (plus de 3 ou 4 modèles), vous risquez effectivement de vous retrouver avec un fichier views.py d'une longueur désagréable. Il est donc intéressant de diviser ce fichier en plusieurs sous fichiers pour répartir la logique en fonction de vos modèles.

Et vous le savez :

    Diviser (views.py) pour mieux régner.

Plus globalement, l'arborescence d'un fresh django project est pas top top. Il existe, par exemple, un truc appelé cookiecutter qui permet d'avoir un django plus facile à déployer par la suite.

--> https://cookiecutter-django.readthedocs.io/en/latest/

Pour plus d'infos, demander à Julien ou Yoan, moi je ne l'ai jamais utilisé

Mais en gros, voici la recette :

- Créez un dossier views et supprimer le fichier views.py
- Ajoutez un fichier **init**.py pour faire du dossier un "package" python utilisable
- Créez vos X fichiers views en fonction des X modèles (task_views.py, step_views.py, etc)
  - Comme ici https://github.com/Ishydo/snapventure/tree/master/snapventure-backend/snapventure/views
- Dans les routes, ne pas oublier de faire appel aux fichiers qui sont désormais dans le package views et non plus au fichiers views.py (qui n'existe plus) !
  - Comme ici : https://github.com/Ishydo/snapventure/blob/master/snapventure-backend/snapventure/urls.py

Codez vos views dans le bonheur et la clarté d'un code aéré 😍
