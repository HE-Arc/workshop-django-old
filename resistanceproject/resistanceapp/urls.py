from django.urls import path
from django.contrib import admin

from . import views

# TODO-ADV-1-3 Uncomment thos four lines used by restframework
#from rest_framework import routers
#router = routers.DefaultRouter()
#router.register('users', views.UserViewSet)
#router.register('soldiers', views.SoldierViewSet)


urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard/', views.DashboardView.as_view(), name='dashboard'),

    # TODO-3-1 - Add route for the previously created soldier list view. Name it soldiers-list
    # TODO-3-3 - Add route for the previously created soldier detail view. Name soldier-detail

    # TODO-4-1 - Add route for the previously created soldier create view
    # TODO-4-3 - Add route for the previously created soldier update view
    # TODO-4-5 - Add route for the previously created soldier delete view

    # TODO-8-1 - Add route for SoldierDeadOnTheField

    # TODO-ADV-1-4 Add restframework API router urls
]
