from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.urls import reverse_lazy

from.models import Soldier

# Create your views here.

def index(request):
    context = {}
    return render(request, 'resistanceapp/index.html', context)


class SoldierListView(generic.ListView):
    model = Soldier

    def get_queryset(self):
        return Soldier.objects.all()

class SoldierDetailView(generic.DetailView):
    model = Soldier

class SoldierCreateView(generic.CreateView):
    model = Soldier
    fields = ['name', 'age', 'strength']

class SoldierUpdateView(generic.UpdateView):
    model = Soldier
    fields = ['name', 'age', 'strength']

class SoldierDeleteView(generic.DeleteView):
    model = Soldier
    success_url = reverse_lazy('dashboard')
