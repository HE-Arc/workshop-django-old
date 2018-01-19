from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.urls import reverse_lazy

from.models import Soldier, Category

# Create your views here.

def index(request):
    context = {}
    return render(request, 'resistanceapp/index.html', context)

class DashboardView(generic.TemplateView):
    template_name = "resistanceapp/dashboard.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['best_soldiers'] = Soldier.objects.order_by('-strength')[:3]
        context['soldiers'] = Soldier.objects.select_related('category').all()
        context['nb_alive'] = Soldier.objects.filter(alive=True).count()
        context['nb_dead'] = Soldier.objects.filter(alive=False).count()
        return context

class SoldierListView(generic.ListView):
    model = Soldier

    def get_queryset(self):
        return Soldier.objects.select_related('category').all()

class SoldierDetailView(generic.DetailView):
    model = Soldier

class SoldierCreateView(generic.CreateView):
    model = Soldier
    fields = ['name', 'category', 'alive', 'age', 'strength']
    success_url = reverse_lazy('dashboard')

class SoldierUpdateView(generic.UpdateView):
    model = Soldier
    fields = ['name', 'category', 'alive', 'age', 'strength']
    success_url = reverse_lazy('dashboard')

class SoldierDeleteView(generic.DeleteView):
    model = Soldier
    success_url = reverse_lazy('dashboard')
