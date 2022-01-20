from django.urls import path
from django.contrib import admin

from . import views

# TODO-ADV-1-3 Add a rest_framework router to register the 2 new viewsets that you've created


urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard/', views.DashboardView.as_view(), name='dashboard'),

    # TODO-3-1 - Add route for the previously created soldier list view. Name it soldiers-list
    path('dashboard/soldiers/',views.SoldierListView.as_view(),name="soldiers-list"),
    # TODO-3-3 - Add route for the previously created soldier detail view. Name soldier-detail
    path('dashboard/soldiers/<pk>/',views.SoldierDetailView.as_view(),name="soldiers-detail"),
    # TODO-4-1 - Add route for the previously created soldier create view
    # TODO-4-3 - Add route for the previously created soldier update view
    # TODO-4-5 - Add route for the previously created soldier delete view

    # TODO-8-1 - Add route for SoldierDeadOnTheField

    # TODO-ADV-1-4 Add restframework API router urls
]
