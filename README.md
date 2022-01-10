# README ONLY IF NEEDED

**WARNING** This README is meant to be visualized in "preview" mode, ideally on Github or in any other preview mode that can read and interprete MarkDown.  
If you open and follow this file in your IDE like VSCode, you could have some troubles with copy-past, etc.  
It's not a big deal, you just need to be informed and adapt certain element if you read the raw content of this file.

## Installing a package

```
pip install django-bootstrap4
pip freeze
pip freeze > requirements.txt
```

> If you are in `resistanceproject` folder the last command has to be replaced by: `pip freeze > ../requirements.txt`

TODO-0-0

`bootstrap4`

TODO-0-1

```
{% load bootstrap4 %}
{% bootstrap_css %}
{% bootstrap_javascript jquery='full' %}
```

## First django model

https://docs.djangoproject.com/fr/3.2/ref/models/fields/#field-types  
https://docs.djangoproject.com/fr/3.2/topics/migrations/

TODO-1-0

```
class Soldier(models.Model):
    name=models.CharField(max_length=200)
    age=models.IntegerField()
    strength=models.IntegerField()
    description=models.TextField()
    alive=models.BooleanField(default=True)
```

TODO-1-1

```
class Soldier(models.Model):

    (...)

    def __str__(self):
        return self.name
```

TODO-1-2

`python manage.py makemigrations resistanceapp`

TODO-1-3

`python manage.py migrate`

TODO-1-4

`admin.site.register(Soldier)`

## Play with data

https://docs.djangoproject.com/fr/3.2/ref/django-admin/#createsuperuser  
https://docs.djangoproject.com/fr/3.2/howto/initial-data/

TODO-2-0

`python manage.py createsuperuser`

TODO-2-1

`localhost:8000/admin and etc`

TODO-2-2

`python manage.py dumpdata resistanceapp.Soldier > resistanceapp/fixtures/soldiers.json --indent=4`

TODO-2-3

Go on the django admin and delete everything

`python manage.py loaddata soldiers`

## List and details features

https://docs.djangoproject.com/fr/3.2/topics/class-based-views/

TODO-3-0

```
class SoldierListView(generic.ListView):
    model = Soldier

    def get_queryset(self):
        return Soldier.objects.all()
```

TODO-3-1

`path('dashboard/soldiers/', views.SoldierListView.as_view(), name='soldiers-list'),`

TODO-3-2

```
class SoldierDetailView(generic.DetailView):
    model = Soldier
```

TODO-3-3

`path('dashboard/soldiers/<pk>/', views.SoldierDetailView.as_view(), name='soldiers-detail'),`

TODO-3-4

Use `object_list` and (`soldier` or `object`)

Some examples:

- `{{ soldier.id }}`
- `{% url 'soldiers-detail' soldier.id %}`
- `{% for soldier in object_list %}`

## Create update delete

https://docs.djangoproject.com/fr/3.2/topics/forms/

TODO-4-0

```
class SoldierCreateView(generic.CreateView):
    model = Soldier
    fields = ['name', 'alive', 'age', 'strength']
    success_url = reverse_lazy('soldiers-list')
```

TODO-4-1

`path('dashboard/soldier/new/', views.SoldierCreateView.as_view(), name='soldiers-new'),`

TODO-4-2

```
class SoldierUpdateView(generic.UpdateView):
    model = Soldier
    fields = ['name', 'alive', 'age', 'strength']
    success_url = reverse_lazy('soldiers-list')
```

TODO-4-3

`path('dashboard/soldier/<pk>/update/', views.SoldierUpdateView.as_view(), name='soldiers-update'),`

TODO-4-4

```
class SoldierDeleteView(generic.DeleteView):
    model = Soldier
    success_url = reverse_lazy('soldiers-list')
```

TODO-4-5

`path('dashboard/soldier/<pk>/delete/', views.SoldierDeleteView.as_view(), name='soldiers-delete'),`

TODO-4-6

Only display. Urls update

## Add categories support

TODO-5-0

```
class Category(models.Model):
    name=models.CharField(max_length=200)
    description=models.TextField()

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name
```

Todo-5-2

```
admin.site.register(Category)
```

TODO-5-4

Add this to Soldier class model

```
category=models.ForeignKey('Category', on_delete=models.CASCADE)
```

TODO-5-5

If you select (1.) when running makemigrations command, be sure to create  
at least one category and put 1 as default value.

If you select (2.) when running makemigrations command, be sure to create  
at least one category and go add default=1 in the Soldier class model.

TODO-5-6

category

## Queries

https://docs.djangoproject.com/en/3.2/topics/db/queries/

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

## Model class methods

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

`{{ b.get_efficiency|floatformat:3 }}`

`{{ b.is_old }}`

## Base View for special actions (not part of the default "resource"/"model")

TODO-8-0

```
class SoldierDeadOnTheField(View):
    def post(self, request):
        print("SOLDIER DEAD ON THE FIELD RIP")
        s = Soldier.objects.get(pk=request.POST.get("soldier_id"))
        s.alive = False
        s.save()
        return redirect('soldiers-list')
    def get(self, request):
        return HttpResponse('Unauthorized! GET never killed any one.', status=401)
```

TODO-8-1

```
path('dashboard/soldier/dead-on-the-field/', views.SoldierDeadOnTheField.as_view(), name='soldiers-dead'),
```

TODO-8-2

```
{% if soldier.alive %}
<form method="post" action="{% url 'soldiers-dead' %}">
  {% csrf_token %}
  <input type="hidden" name="soldier_id" value="{{ soldier.id }}">
  <button type="submit" class="btn btn-danger btn-sm">Kill :(</button>
</form>
{% endif %}
```

## Advanced Django REST Framework

TODO-ADV-1-0

```
pip install djangorestframework
```

```
rest_framework
```

TODO-ADV-1-1

```
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email')

class SoldierSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Soldier
        fields = ('name', 'age', 'strength', 'description', 'alive')
```

TODO-ADV-1-2

```
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class SoldierViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Soldier.objects.all()
    serializer_class = SoldierSerializer
```

TODO-ADV-1-3

```
from rest_framework import routers
router = routers.DefaultRouter()
router.register('users', views.UserViewSet)
router.register('soldiers', views.SoldierViewSet)
```

TODO-ADV-1-4

```
path('api/v1/', include(router.urls))
```

## Advanced play with signals

TODO-ADV-2-0

```
def soldier_post_save(sender, **kwargs):
    print("SOLDIER WAS SAVED IN THE SYSTEM")


def soldier_post_delete(sender, **kwargs):
    print("SOLDIER HAS BEEN DELETED")
```

TODO-ADV-2-1

```
post_save.connect(soldier_post_save, sender=Soldier)
post_delete.connect(soldier_post_delete, sender=Soldier)
```
