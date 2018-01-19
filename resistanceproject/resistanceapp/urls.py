from django.urls import path
from django.contrib import admin

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard', views.SoldierListView.as_view(), name='dashboard'),
    path('dashboard/soldier/new', views.SoldierCreateView.as_view(), name='soldier-new'),
    path('dashboard/soldier/<pk>/', views.SoldierDetailView.as_view(), name='soldier-detail'),
    path('dashboard/soldier/<pk>/update', views.SoldierUpdateView.as_view(), name='soldier-update'),
    path('dashboard/soldier/<pk>/delete', views.SoldierDeleteView.as_view(), name='soldier-delete'),
]
