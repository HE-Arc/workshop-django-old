from django.db import models

from django.db.models.signals import post_save



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

post_save.connect(soldier_post_save, sender=Soldier)
