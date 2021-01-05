# demo-django-resistance-app

Let's resist the rails empire with django 3! A mini workshop to introduce the django web framework.

# Dépendances

## Python

version >= 3.6
Requirement comming from Django : https://docs.djangoproject.com/en/3.1/releases/3.1/#python-compatibility

I used Python 3.8.2
```
python --version
```

## pip

I used v20.3
```
pip --version
```

Upgrade your pip with
```
python -m pip install --upgrade pip
```

# Installation et configuration

## Comment démarrer

Vous trouverez ci-dessous les quelques commandes qui vous permettront de commencer à travailler sur le workshop.

1. D'abord on clone le répo et on checkout sur la bonne branche, bon ça vous connaissez c'est ez ;)

```
git clone https://github.com/HE-Arc/demo-django-resistance-app.git .
git checkout todo-resistance-app
```

2. Ensuite on va créer un environement virtuel (= virtual environement = venv), cela est extrèmement important !

Django n'utilise pas de gestionnaire de paquets comme npm, yarn ou composer. Il va donc falloir le faire nous même (mais pas d'inquiètude tout pourra ensuite être quasi-automatisé sur votre IDE - En tout cas c'est possible sur VSCode, si vous utilisez des trucs bizarres, ça sera à vous de trouvez comment faire ou alors utiliser les procédures manuelles ;))

Le venv permet d'isoler les bibliothèques (requirements) que l'on a besoin dans ce projet et ainsi d'éviter d'avoir des conflits avec d'autres projets. C'est donc absolument vitale et nécessaire de faire un environement virtuel pour chacun de vos projet Django. Vous me remercierez plus tard d'insister à ce point - *Trust me! C'est important.*

Il existe plusieurs bibliothèques qui permettent toutes de créer des environements virtuels, utilisez celui que vous souhaitez, ça ne devrait rien changer. Personnellement j'utilise celui disponible directement avec Python.

Vous devez le créer une fois au début et/ou à chaque fois que vous clonez le projet **IMPORTANT : l'environement virtuel ne dois JAMAIS être push !** Ensuite une fois qu'il est créer pour la première fois vous n'aurez plus qu'a l'activez, là encore attention il ne faut pas oubliez de le réactiver. Vous pouvez checker que vous avez bien l'extension VSCode "Python" (sinon installez là)

```
python -m venv .venv
source .venv/Scripts/activate
```

3. On installe les requirements dans notre venv, bon là il existe d'autres techniques.

Il existe des débâts sur le net au sujet d'une meilleure utilisation de se fichier.  
Est-ce que c'est bien d'avoir un fichier "requirements.txt" ou autre chose ?

Vous verrez que vous aurez quelques soucis d'utilisation avec se fichier, car vous devez l'update à chaque fois que ajoutez, modifiez ou supprimez quelque chose dedans, mais bon c'est pas non plus trop compliqué, il suffit de suivre une certaine méthode et si vous êtes méthodique, il n'y aura aucun soucis.

J'ai l'habitude d'utiliser cela, et c'est une technique qui est encore dans la très grande majoritée des cas utilisés et je pense que c'est mieux si vous vous familiarisez au moins une fois avec cette utilisation car c'est celle que vous allez rencontrer quasi partout, mais si ça vous intéresse vous pouvez aller checker pour voir si il n'existe pas une meilleure technique.

```
pip install -r requirements.txt
```

4. Finalement déplacez-vous dans le projet et démarrez le serveur

> Il est possible de structurer son projet différement, la structure que nous allons utilisez est celle proposez par défaut dans Django, donc encore une fois, c'est bien si essayez de vous familiarisez avec celle. Une fois que vous aurez compris et que vous serez à l'aise n'hésitez pas à chercher comment l'améliorer et l'adapter au mieux pour votre projet.

```
cd resistanceproject
python manage.py runserver
```

Si vous voyez du rouge après la dernière commande (un truc de migrations) et une erreur en atteignant `localhost:8000`... C'est que c'est tout bon !

## There's no magic

Ici vous avez un répo avec un projet déjà existant, en réalité c'est juste pour nous faire gagner un peu de temps, mais c'est extrèmement simple à reproduire. Voici donc les premières étapes que vous devrez suivre afin de créer un nouveau projet de zéro (Si ce n'était pas assez, les étapes qui vont suivre ne doivent PAS être effectué pour ce workshop, c'est à faire si vous commencez un nouveau projet):

1. Créer un dossier et déplacez-vous y.

2. S'assurer d'avoir la bonne version de python et de pip pour la version de Django que vous souhaitez utiliser

3. Créer un environement virtuel (venv)

```
python -m venv .venv
source .venv/Scripts/activate
```

4. Installer Django

```
pip install Django
```

5. Créer le projet Django et déplacez vous y

```
django-admin startproject resistanceproject
cd resistanceproject
```

6. Créer votre première app et démarrez les migrations de base

Ici le nom des apps et des projets ont été choisi pour être correspondre au workshop, mais vous pouvez nommez votre projet et vos apps en fonction de votre projet évidemment.

```
python manage.py startapp resistanceapp
python manage.py migrate
```

# Méthodologie

L'app est pré-existante. Il faudra remplir les trous (TODOs) pour la rendre fonctionnelle (eeeasy!).

On part de TODO-0-X jusqu'à TODO-7-X, avec à chaque étape quelques lignes à taper.

On fait une recherche dans l'arborescence (Ctrl+Shift+F avec VSCode p.ex) et on recherche les TODOS un à un.

Les réponses se trouvent dans le README sur la branche `todo-resistance-app` mais **c'est de la triche de regarder**. C'est seulement en cas d'urgence (je vous vois).
