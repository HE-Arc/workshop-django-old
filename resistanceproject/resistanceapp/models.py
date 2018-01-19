from django.db import models

# Create your models here.
class Soldier(models.Model):
    name=models.CharField(max_length=200)
    age=models.IntegerField()
    strength=models.IntegerField()
    description=models.TextField()

    def __str__(self):
        return self.name
