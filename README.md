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

# All anwers from todo :

## Installing a package

TODO-0-0 `bootstrap4`

TODO-0-1

```
{% load bootstrap4 %}
{% bootstrap_css %}
{% bootstrap_javascript jquery='full' %}
```

## First django model

TODO-1-1

```
class Soldier(models.Model):
    name=models.CharField(max_length=200)
    age=models.IntegerField()
    strength=models.IntegerField()
    description=models.TextField()
    alive=models.BooleanField(default=True)

    def __str__(self):
        return self.name
```

TODO-1-2 `python manage.py makemigrations resistanceapp`

TODO-1-3 `python manage.py migrate`

TODO-1-4 `admin.site.register(Soldier)`

## Play with data

TODO-2-0 `python manage.py createsuperuser`

TODO-2-1 `localhost:8000/admin and etc`

TODO-2-2 `python manage.py dumpdata resistanceapp.Soldier > resistanceapp/fixtures/soldiers.json`


TODO-2-3

Go on the django admin and delete everything

`python manage.py loaddata soldiers`


## List and details features

TODO-3-0

```
class SoldierListView(generic.ListView):
    model = Soldier

    def get_queryset(self):
        return Soldier.objects.all()
```


TODO-3-1

`    path('dashboard/soldiers', views.SoldierListView.as_view(), name='dashboard-soldiers'),`


TODO-3-2

```
class SoldierDetailView(generic.DetailView):
    model = Soldier
```


TODO-3-3

`path('dashboard/soldier/<pk>/', views.SoldierDetailView.as_view(), name='soldier-detail'),
  `

TODO-3-4

It's only display. Use urls and your brain for some {{ soldier.xx }}



## Create update delete

TODO-4-0

```
class SoldierCreateView(generic.CreateView):
    model = Soldier
    fields = ['name', 'alive', 'age', 'strength']
    success_url = reverse_lazy('dashboard')
```

TODO-4-1 `path('dashboard/soldier/new', views.SoldierCreateView.as_view(), name='soldier-new'),
  `

TODO-4-2

```
class SoldierUpdateView(generic.UpdateView):
    model = Soldier
    fields = ['name', 'alive', 'age', 'strength']
    success_url = reverse_lazy('dashboard')
```

TODO-4-3 `path('dashboard/soldier/<pk>/update', views.SoldierUpdateView.as_view(), name='soldier-update'),
  `

TODO-4-4

```
class SoldierDeleteView(generic.DeleteView):
    model = Soldier
    success_url = reverse_lazy('dashboard')
```
TODO-4-5

`path('dashboard/soldier/<pk>/delete', views.SoldierDeleteView.as_view(), name='soldier-delete'),
  `

TODO-4-6

Only display. Urls update


## Add categories support

TODO-5-0

```
class Category(models.Model):
    name=models.CharField(max_length=200)
    description=models.TextField()

    def __str__(self):
        return self.name
```

TODO-5-1

```
add this
    category=models.ForeignKey('Category', on_delete=models.CASCADE)
```

Create new model category

Todo-5-4
```
admin.site.register(Category)
```

TODO-5-5

category

## Queries

TODO-6-0

```
def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['categories'] = Category.objects.all()
    context['best_soldiers'] = Soldier.objects.order_by('-strength')[:3]
    context['nb_alive'] = Soldier.objects.filter(alive=True).count()
    context['nb_dead'] = Soldier.objects.filter(alive=False).count()
    return context
```


## Advanced

TODO-7-1

```
def get_efficiency(self):
    return self.strength / self.age
```

TODO-7-2

```
def is_old(self):
      return self.age > 60
```

TODO-7-3

`
{{ soldier.get_efficiency|floatformat:3 }}
`


## Advanced play with signals

TODO-ADV-0

```
def soldier_post_save(sender, **kwargs):
    print("SOLDIER WAS SAVED IN THE SYSTEM")


def soldier_post_delete(sender, **kwargs):
    print("SOLDIER HAS BEEN DELETED")
```

TODO-ADV-1

```
post_save.connect(soldier_post_save, sender=Soldier)
post_delete.connect(soldier_post_delete, sender=Soldier)
```
