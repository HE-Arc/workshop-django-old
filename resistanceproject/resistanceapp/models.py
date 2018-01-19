from django.db import models

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

class Category(models.Model):
    name=models.CharField(max_length=200)
    description=models.TextField()

    def __str__(self):
        return self.name
