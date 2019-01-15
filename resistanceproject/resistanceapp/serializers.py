from django.contrib.auth.models import User
from resistanceapp.models import Soldier

from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email')

class SoldierSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Soldier
        fields = ('name', 'age', 'strength', 'description', 'alive')
