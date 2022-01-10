from django.db import models
from django.db.models.signals import post_save, post_delete


# TODO-1-0 - Create Soldier model with name, age, strength, description and alive
# TODO-1-1 - Add __str__ override for a representation with the name of the soldier
class Soldier(models.Model):
    category=models.ForeignKey('Category', on_delete=models.CASCADE, default=1)
    name=models.CharField(max_length=200)
    age=models.IntegerField()
    strength=models.IntegerField()
    description=models.TextField()
    alive=models.BooleanField(default=True)

    def __str__(self):
        return self.name

# TODO-1-2 - When the model definition is ready, generate the migration (> python manage.py ...)
# TODO-1-3 - When the migration is generated, apply them (> python manage.py ...)

# TODO-2-0 - Create a superuser for the django admin (> python manage.py ...)
# TODO-2-1 - Try the django-admin to create some entries in your DB (localhost:8000/admin)
# TODO-2-2 - Export your data to automatically create a fixture (> python manage.py ...)
# TODO-2-3 - Delete your previously created entries from the django-admin and RELOAD them with the fixture

    # TODO-7-1 - Add a class method to get the efficiency (strength / age) of a soldier
    def get_efficiency(self):
        return self.strength / self.age
    # TODO-7-2 - Add a class method to get if a soldier is old or not (age > 60 is old)
    def is_old(self):
      return self.age > 60


# TODO-5-1 - Generate migration, apply migration
# TODO-5-3 - Add some categories from django admin
# TODO-5-4 - Add category field foreign key to soldier
# TODO-5-5 - Generate migration, apply migration, IMPORTANT : if you already have Soldiers in your DB you'll have to give a default value.

# TODO-5-0 - Create category model with name and description fields with __str__ override
class Category(models.Model):
    name=models.CharField(max_length=200)
    description=models.TextField()
    
    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

# TODO-ADV-2-0 - Create two methods that will be triggered on specific signals
# TODO-ADV-2-1 - Connect the post_save and post_delete signals of Soldier model to your methods
