from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import generic, View
from django.urls import reverse_lazy

from .models import Soldier, Category

# Create your views here.
def index(request):
    context = {}
    return render(request, 'resistanceapp/index.html', context)

class DashboardView(generic.TemplateView):
    template_name = "resistanceapp/dashboard.html"

    # TODO-6-0 - Write queries for categories, 3 best soldiers by strength, count alive soldiers, count dead soldiers
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['best_soldiers'] = Soldier.objects.order_by('strength').reverse()[:3]
        context['nb_alive_soldiers'] = Soldier.objects.filter(alive=True).count()
        context['nb_dead_soldiers'] = Soldier.objects.filter(alive=False).count()
        
        return context


    # TODO-3-0 Create the soldier list view with django class based views
class SoldierListView(generic.ListView):
    model=Soldier
    #def get_queryset(self):
    #   return Soldier.objects.all()

    # TODO-3-2 Create the soldier detail view with django class based views
class SoldierDetailView(generic.DetailView):
    model = Soldier
    # TODO-4-0 - Create the soldier create view with django class based views
class SoldierCreateView(generic.CreateView):
    model = Soldier
    fields = ['name','age','description','strength','alive','category']
    success_url = reverse_lazy('dashboard-soldiers')

    # TODO-4-2 - Create the soldier update view with django class based views
class SoldierUpdateView(generic.UpdateView):
    model = Soldier
    fields = ['name','age','description','strength','alive','category']
    success_url = reverse_lazy('dashboard-soldiers')
    # TODO-4-4 - Create the soldier delete view with django class based views
class SoldierDeleteView(generic.DeleteView):
    model = Soldier
    success_url = reverse_lazy('dashboard-soldiers')
    # TODO-5-6 - Add category field for soldier to create and update views


    #TODO-8-0 - Write a view to set a soldier dead :( (sad)
class SoldierDeadOnTheField(View):

    def post(self,request):
        print("deadSoldier")
        soldier = Soldier.objects.get(pk=request.POST.get('soldier_id'))
        soldier.alive = False
        soldier.save()
        return redirect('dashboard-soldiers')

    def get(self,request):
        return HttpResponse("Unauthorized, Don't kill the soldier",status=405)
class SoldierResucite(View):

    def post(self,request):
        print("aliveSoldier")
        soldier = Soldier.objects.get(pk=request.POST.get('soldier_id'))
        soldier.alive = True
        soldier.save()
        return redirect('dashboard-soldiers')

    def get(self,request):
        return HttpResponse("Unauthorized, Don't resucite the soldier",status=405)

    # TODO-ADV-1-2 - Write views using your serializers https://www.django-rest-framework.org/tutorial/quickstart/#views
