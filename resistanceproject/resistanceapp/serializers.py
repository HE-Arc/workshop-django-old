from django.contrib.auth.models import User
from resistanceapp.models import Soldier

from rest_framework import serializers

# TODO-ADV-1-1 Write serializers for User and Soldier models https://www.django-rest-framework.org/tutorial/quickstart/#serializers
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email')

class SoldierSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Soldier
        fields = ('name', 'age', 'strength', 'description', 'alive')