from django.urls import path
from django.contrib import admin

from . import views

from django.urls import include

# TODO-ADV-1-3 Add a rest_framework router to register the 2 new viewsets that you've created
from rest_framework import routers
router = routers.DefaultRouter()
router.register('users', views.UserViewSet)
router.register('soldiers', views.SoldierViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard/', views.DashboardView.as_view(), name='dashboard'),

    # TODO-3-1 - Add route for the previously created soldier list view. Name it soldiers-list
    path('dashboard/soldiers/',views.SoldierListView.as_view(),name="soldiers-list"),
    # TODO-4-1 - Add route for the previously created soldier create view
    path('dashboard/soldiers/new/',views.SoldierCreateView.as_view(),name="soldiers-new"),
    # TODO-8-1 - Add route for SoldierDeadOnTheField
    path('dashboard/soldiers/commit-not-alive/',views.SoldierKillView.as_view(),name="soldiers-kill"),
    # TODO-3-3 - Add route for the previously created soldier detail view. Name soldier-detail
    path('dashboard/soldiers/<pk>/',views.SoldierDetailView.as_view(),name="soldiers-detail"),
    # TODO-4-3 - Add route for the previously created soldier update view
    path('dashboard/soldiers/<pk>/update',views.SoldierUpdateView.as_view(),name="soldiers-update"),
    # TODO-4-5 - Add route for the previously created soldier delete view
    path('dashboard/soldiers/<pk>/delete',views.SoldierDeleteView.as_view(),name="soldiers-delete"),

    # TODO-ADV-1-4 Add restframework API router urls
    path('api/v1/', include(router.urls)),
]
