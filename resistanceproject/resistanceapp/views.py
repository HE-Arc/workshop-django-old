from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import generic, View
from django.urls import reverse_lazy

from .models import Soldier, Category

from django.contrib.auth.models import User
from .serializers import UserSerializer, SoldierSerializer
from rest_framework import viewsets

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

class SoldierDeadOnTheField(View):
    def post(self, request):
        print("SOLDIER DEAD ON THE FIELD RIP")
        s = Soldier.objects.get(pk=request.POST.get("soldier_id"))
        s.alive = False
        s.save()
        return redirect('dashboard-soldiers')
    def get(self, request):
        return HttpResponse('Unauthorized, don\'t try to kill my soldiers please.', status=401)


# This is API related for demo
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
