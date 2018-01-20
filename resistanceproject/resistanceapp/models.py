from django.db import models
from django.db.models.signals import post_save, post_delete


# Create your models here.
class Soldier(models.Model):
    name=models.CharField(max_length=200)
    age=models.IntegerField()
    strength=models.IntegerField()
    description=models.TextField()
    category=models.ForeignKey('Category', on_delete=models.CASCADE)
    alive=models.BooleanField(default=True)

    def __str__(self):
        return self.name

    def get_efficiency(self):
        return self.strength / self.age

    def is_old(self):
        return self.age > 60

class Category(models.Model):
    name=models.CharField(max_length=200)
    description=models.TextField()

    def __str__(self):
        return self.name



def soldier_post_save(sender, **kwargs):
    print("SOLDIER WAS SAVED IN THE SYSTEM")


def soldier_post_delete(sender, **kwargs):
    print("SOLDIER HAS BEEN DELETED")

post_save.connect(soldier_post_save, sender=Soldier)
post_delete.connect(soldier_post_delete, sender=Soldier)
